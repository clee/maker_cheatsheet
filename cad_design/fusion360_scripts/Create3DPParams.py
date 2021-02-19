#Author-Grégoire Saunier
#Description-Creates basic parameters for 3D printing Bear projects

import adsk.core, adsk.fusion, traceback

paramsToAdd = [
    ['layer_height',     '0.2',                                   'mm', ''],
    ['e_width',          '0.45',                                  'mm', 'extrusion_width'],
    ['e_spacing',        'e_width - layer_height * (1 - 3.14/4)', 'mm', 'extrusion spacing according to PrusaSlicer default settings'],
    ['num_perimeters',   '4',                                     '',   'number of perimeters'],
    ['num_tops_bottoms', '5',                                     '',   'number of top and bottom layers'],
    ['m3_hole',          '3.3',                                   'mm', 'M3 hole diameter'],
    ['m3_head',          '5.8',                                   'mm', 'M3 screw ISO4762 head diameter'],
    ['m3_thread',        '2.7',                                   'mm', 'M3 self threading hole diameter'],
    ['m3_hex_nut',       '6.2',                                   'mm', 'M3 hex nut ISO4032 inscribed diameter'],
    ['m3_square_nut',    '5.5',                                   'mm', 'M3 square nut DIN562 pocket width'],
    ['m5_hole',          '5.3',                                   'mm', 'M5 hole diameter'],
    ['m5_head',          '10',                                    'mm', 'M5 screw ISO4762 head diameter'],
]

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active Fusion design')
            return

        params = design.userParameters
        for paramNum in range(len(paramsToAdd)) :
            print(paramsToAdd[paramNum][0])
            params.add(paramsToAdd[paramNum][0], adsk.core.ValueInput.createByString(paramsToAdd[paramNum][1]), paramsToAdd[paramNum][2], paramsToAdd[paramNum][3])
        
        ui.messageBox('Parameters have been created successfully')


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))