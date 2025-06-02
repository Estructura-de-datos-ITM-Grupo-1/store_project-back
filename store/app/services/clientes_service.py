import os
import json
from datetime import datetime
from typing import List
from app.core.paths import CLIENTES_JSON as ARCHIVO_CLIENTES
from app.core.paths import AUDITORIA_CLIENTES_JSON as ARCHIVO_AUDITORIA

# Roles autorizados para operaciones en clientes
ROLES_PERMITIDOS = ['administrador', 'comercial']

# Seguridad 

def verificar_rol(rol: str):
    if rol not in ROLES_PERMITIDOS:
        raise PermissionError("Acceso denegado: Rol no autorizado.")

# Utilidades

def leer_clientes() -> List[dict]:
    try:
        with open(ARCHIVO_CLIENTES, mode='r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def escribir_clientes(clientes: List[dict]):
    with open(ARCHIVO_CLIENTES, mode='w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

# Registro de auditoría 

def registrar_auditoria(id_cliente: str, accion: str, usuario: str, campo: str = '', valor_anterior: str = '', valor_nuevo: str = ''):
    try:
        with open(ARCHIVO_AUDITORIA, mode='r', encoding='utf-8') as f:
            auditoria = json.load(f)
    except FileNotFoundError:
        auditoria = []

    nueva_entrada = {
        'fecha_hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'id_cliente': id_cliente,
        'accion': accion.upper(),
        'usuario': usuario,
        'campo': campo,
        'valor_anterior': valor_anterior,
        'valor_nuevo': valor_nuevo
    }
    auditoria.append(nueva_entrada)

    with open(ARCHIVO_AUDITORIA, mode='w', encoding='utf-8') as f:
        json.dump(auditoria, f, indent=4, ensure_ascii=False)

# Funcionalidades del módulo 

def registrar_cliente(rol: str, nombre: str, tipo_id: str, numero_id: str, telefono: str, email: str, direccion: str):
    verificar_rol(rol)
    clientes = leer_clientes()
    nuevo_id = str(len(clientes) + 1)
    cliente = {
        'id': nuevo_id,
        'nombre': nombre,
        'tipo_id': tipo_id,
        'numero_id': numero_id,
        'telefono': telefono,
        'email': email,
        'direccion': direccion,
        'estado': 'activo'
    }
    clientes.append(cliente)
    escribir_clientes(clientes)
    registrar_auditoria(nuevo_id, 'registro', rol)
    return cliente

def modificar_cliente(rol: str, cliente_id: str, campo: str, nuevo_valor: str):
    verificar_rol(rol)
    clientes = leer_clientes()
    for cliente in clientes:
        if cliente['id'] == cliente_id and cliente['estado'] == 'activo':
            if campo in cliente:
                valor_anterior = cliente[campo]
                cliente[campo] = nuevo_valor
                registrar_auditoria(cliente_id, 'modificacion', rol, campo, valor_anterior, nuevo_valor)
                escribir_clientes(clientes)
                return cliente
    raise ValueError("Cliente no encontrado o inactivo.")

def inactivar_cliente(rol: str, cliente_id: str):
    verificar_rol(rol)
    clientes = leer_clientes()
    for cliente in clientes:
        if cliente['id'] == cliente_id and cliente['estado'] != 'inactivo':
            cliente['estado'] = 'inactivo'
            registrar_auditoria(cliente_id, 'inactivacion', rol)
            escribir_clientes(clientes)
            return cliente
    raise ValueError("Cliente no encontrado o ya estaba inactivo.")

def listar_clientes_activos() -> List[dict]:
    clientes = leer_clientes()
    return [c for c in clientes if c['estado'] == 'activo']
