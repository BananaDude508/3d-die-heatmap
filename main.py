from os.path import basename
from vpython import *
from polyhedra import *
from vpextensions.colors import *
from vpextensions.triangles import *
import document_reader as dr
from pathlib import Path

data_path = dr.data_path
template_data_path = dr.data_path + '\\Template.xlsx'
downloads_path = str(Path.home() / "Downloads")

target_frame_rate = 60

weightmaps = dr.get_frequencies_from_file(0)

ico = Icosahedron()
dod = Dodecahedron()
decT = Decahedron(1)
decU = Decahedron()
oct = Octahedron()
cube = Cube()
tet = Tetrahedron()

dice = [ico, dod, decT, decU, oct, cube, tet]

active_die = dice[0]
active_die.weightmap = weightmaps[0]
active_die.draw_shape()

ws_buttons = []
def refresh_data_options():
    global ws_buttons

    for ws_button in ws_buttons:
        ws_button.delete()

    ws_buttons = []

    dr.all_xl_files = dr.find_all_xl_files()
    for index,name in enumerate([basename(f) for f in dr.all_xl_files]):
        ws_buttons.append(button(text=name[:name.rindex('.')], bind=load_new_file, id=index))  
    
upload_text = wtext(text='.xlsx data path is '+data_path)
scene.append_to_caption('\n')
refresh_button = button(text='Refresh data options', bind=refresh_data_options)

def delete_shape(shape):
    for label in shape.labels:
        label.visible = False
        del label 
    shape.labels = []

    for triangle in shape.triangles:
        triangle.visible = False
        del triangle
    shape.triangles = []

    for quad in shape.quads:
        quad.visible = False
        del quad
    shape.quads = []
    
    for cylinder in shape.cylinders:
        cylinder.visible = False
        del cylinder
    shape.cylinders = []

def load_new_file(evt):
    global weightmaps
    global active_die

    if evt.id < len(dr.all_xl_files): 
        weightmaps = dr.get_frequencies_from_file(evt.id)
        delete_shape(active_die)
        active_die.weightmap = weightmaps[dice.index(active_die)]
        active_die.draw_shape()
    
def load_new_die(evt):
    global active_die

    if not evt.id == dice.index(active_die) and evt.id < len(dice):
        delete_shape(active_die)
        active_die = dice[evt.id]
        active_die.weightmap = weightmaps[evt.id]
        active_die.draw_shape()


def main():
    scene.append_to_caption('\n\n')

    die_types = ['D20', 'D12', 'D%', 'D10', 'D8', 'D6', 'D4']
    die_buttons = []
    for index,type in enumerate(die_types):
        die_buttons.append(button(text=type, bind=load_new_die, id=index))
        scene.append_to_caption(' ')

    scene.append_to_caption('\n\n')

    refresh_data_options()

    while True: 
        handle_label_visibility(active_die)

        sleep(1/target_frame_rate)

if __name__ == '__main__':
    main()

