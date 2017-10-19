# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Selection Tab",
           "author": "CDMJ",
           "version": (1, 00),
           "blender": (2, 79, 0),
           "location": "Toolbar > Misc Tab > Selection",
           "description": "Selection tools and methods",
           "warning": "WIP",
           "wiki_url": "",
           "category": "Mesh"}




import bpy

class VertexSelect(bpy.types.Operator):
    """VertexSelect"""
    bl_idname = "mesh.vertex_select"


    bl_label = "Vert Select"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        scene = context.scene


        #new code
        bpy.context.tool_settings.mesh_select_mode = (True, False, False)
        
        return {'FINISHED'}
    
class EdgeSelect(bpy.types.Operator):
    """EdgeSelect"""
    bl_idname = "mesh.edge_select"


    bl_label = "Edge Select"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        scene = context.scene


        #new code
        bpy.context.tool_settings.mesh_select_mode = (False, True, False)
        
        return {'FINISHED'}

class FaceSelect(bpy.types.Operator):
    """Face Select"""
    bl_idname = "mesh.face_select"


    bl_label = "Face Select"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        scene = context.scene


        #new code
        bpy.context.tool_settings.mesh_select_mode = (False, False, True)
        
        return {'FINISHED'}
class PivotSet(bpy.types.Operator):
    """Set Pivot"""
    bl_idname = "mesh.pivot_set"
    bl_label = "Pivot"
    bl_options = { 'REGISTER', 'UNDO'}
    #https://blender.stackexchange.com/questions/1291/change-pivot-or-local-origin-of-an-object
    def execute(self, context):
        saved_location = bpy.context.scene.cursor_location.copy()
        bpy.ops.view3d.snap_cursor_to_selected()

        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')  
        bpy.context.scene.cursor_location = saved_location

        bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}    

    
    
class SelectionPanel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_label = "Selection Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Selection"
    
    def draw(self, context):
        
        layout = self.layout
        layout.label("What to Select")    
        row = layout.row(align=True)
        
        row.alignment = 'EXPAND'
        
        
        #row = layout.row()
        row.operator("mesh.vertex_select", text = "Vertex", icon = 'VERTEXSEL')
        #row = layout.row()
        row.operator("mesh.edge_select", text = "Edge", icon = 'EDGESEL')
        #row = layout.row()
        row.operator("mesh.face_select", text = "Face", icon = 'FACESEL')
        
        layout = self.layout
        row = layout.row(align=True)
        #row.alignment = 'EXPAND'
        row.operator("mesh.region_to_loop", text = "Border", icon = 'SNAP_FACE')
        row.operator("mesh.select_linked", text = "Object", icon = 'MESH_CUBE') 
        row.operator("mesh.pivot_set", text = "Pivot", icon = 'LAYER_ACTIVE')
 
        
        ########generic example#####
        layout = self.layout
        layout.label("Method of Selection")    
        row = layout.row(align=True)
        
        row.alignment = 'EXPAND'
        row.operator("view3d.select_border", text = "Box", icon = 'BORDERMOVE')
        row.operator("view3d.select_circle", text = "Circle", icon = 'FORCE_FORCE')
        row = layout.row()
       

        layout = self.layout
        layout.label("Selection Tools")    
        row = layout.row(align=True)
        
        row.alignment = 'EXPAND' 
        row.operator("mesh.select_all", text= "De/Select all")
        row.operator("mesh.select_nth", text= "Checker Deselect")                   
        

       

def register():
    
    bpy.utils.register_module(__name__)
    

def unregister():
    
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

