import json
import os
from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException
from app.schemas.usuarios_schema import CrearUsuario, ModificarUsuario
from app.models.usuarios_model import Usuario


class Administracion_usuarios:
    def __init__(self):
        self.usuarios = {}
                 
    def crear_usuario(self, nombre_completo, nombre_usuario, contrasena, correo=None, rol=None):
        if nombre_usuario in self.usuarios:
            print("Error: El nombre de usuario ya existe.")
            return
        self.usuarios[nombre_usuario] = Usuario(nombre_completo, nombre_usuario, contrasena, correo, rol)
        print(f"Usuario '{nombre_usuario}' creado exitosamente.")
        
    def modificar_usuario(self, nombre_usuario, nuevo_nombre=None, nueva_contrasena=None, nuevo_correo=None, nuevo_rol=None):
        usuario = self.usuarios.get(nombre_usuario)
        if not usuario:
            print("Error: Usuario no encontrado.")
            return
        elif nuevo_nombre:
            usuario.nombre_completo = nuevo_nombre
        elif nueva_contrasena:
            usuario.contrasena = nueva_contrasena
        elif nuevo_correo is not None:
            usuario.correo = nuevo_correo
        elif nuevo_rol:
            usuario.rol = nuevo_rol
        print(f"Usuario '{nombre_usuario}' modificado correctamente.")
        
    def inactivar_usuario(self, nombre_usuario):
        usuario = self.usuarios.get(nombre_usuario)
        if not usuario:
            print("Error: Usuario no encontrado.")
            return
        usuario.activo = False
        print(f"Usuario '{nombre_usuario}' ha sido inactivado.")
        
    def mostrar_usuarios(self, solo_activos=True):
        for usuario in self.usuarios.values():
            if solo_activos and not usuario.activo:
                continue
            print(usuario)