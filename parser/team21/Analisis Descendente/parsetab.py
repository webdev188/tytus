
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALTER AND AS BETWEEN BIGINT BOOLEAN CARACTER_O_CADENA CHAR CHARACTER CHECK COMA CONSTRAINT CORDER CORIZQ CREATE CUATROPTOS CURRENT_USER DATABASE DATABASES DATE DAY DECIMAL DEFAULT DIFERENTEQ DIVISION DOUBLE DROP ENUM EXISTS FOREIGN HOUR IDENTIFICADOR IF IGUAL ILIKE IN INTEGER INTERVAL IS KEY LIKE LLAVEA LLAVEC MAS MAYORIGUALQ MAYORQ MENORIGUALQ MENORQ MENOS MINUTE MODE MONEY MONTH NOENTERO NOT NULL NUMERIC OR OUT OWNER PARDER PARIZQ POR PORCENTAJE PRECISION PRIMARY PTCOMA PUNTO REAL REFERENCES RENAME REPLACE SECOND SESSION_USER SHOW SIMILAR SMALLINT TABLE TEXT TIME TIMESTAMP TO TYPE UMAS UMENOSCADENA UNIQUE VARCHAR VARYING WITH WITHOUT YEAR ZONE\n    s : instrucciones\n    instrucciones : instruccion instruccionesp\n                       |\n    instruccionesp : instruccion instrucciones\n                        |\n    instruccion : CREATE createp\n                    | ALTER DATABASE alterp\n                    | DROP DATABASE dropp IDENTIFICADOR\n    instruccion : SHOW DATABASES opcional3 PTCOMA\n\n    dropp :   IF EXISTS\n                |\n    alterp :  IDENTIFICADOR alterpp\n\n    alterpp : RENAME TO alterppp\n                | OWNER TO alterppp\n    \n    alterppp : IDENTIFICADOR\n             | CURRENT_USER\n             | SESSION_USER\n\n    \n    createp :  OR REPLACE DATABASE opcional IDENTIFICADOR opcional PTCOMA\n            |  TYPE createpp\n            |  DATABASE createpp\n            |  TABLE createpp\n    \n    createpp : IDENTIFICADOR createtp\n    \n    createtp : SHOW\n\n    l_campos : IDENTIFICADOR l_campo l_campos\n                | COMA IDENTIFICADOR l_campo l_campos\n                |\n    l_campo : tipo l_campo\n                 |\n    tipo : INTEGER\n            | DATE\n            | NOT\n            | NULL\n            | PRIMARY KEY\n            | FOREIGN KEY REFERENCES\n            | CONSTRAINT\n            | UNIQUE\n            | IDENTIFICADOR\n    tipo : VARCHAR PARIZQ NOENTERO PARDER\n            | CHAR PARIZQ NOENTERO PARDER\n            | CHECK PARIZQ expresion PARDER\n    tipo : DECIMAL PARIZQ NOENTERO COMA NOENTERO PARDER\n             | DOUBLE\n             | DECIMAL\n             | NOENTERO\n\n     l_cadenas : PARIZQ CARACTER_O_CADENA l_cadenasp PARDER\n     l_cadenasp : COMA CARACTER_O_CADENA l_cadenasp\n                     |\n    opcional :  IF NOT EXISTS\n                 | OWNER opcional1 IDENTIFICADOR opcional2\n                 |\n    opcional1 : IGUAL\n                  |\n     opcional2 : MODE  opcional1 NOENTERO\n                   |\n\n    opcional3 : LIKE CARACTER_O_CADENA\n                 |\n\n    expresion :  MENOS NOENTERO '
    
_lr_action_items = {'$end':([0,1,2,3,8,9,10,18,20,22,23,24,31,32,33,36,38,49,50,51,52,53,57,],[-3,0,-1,-5,-3,-2,-6,-4,-20,-19,-21,-7,-22,-23,-12,-8,-9,-13,-15,-16,-17,-14,-18,]),'CREATE':([0,3,8,10,20,22,23,24,31,32,33,36,38,49,50,51,52,53,57,],[4,4,4,-6,-20,-19,-21,-7,-22,-23,-12,-8,-9,-13,-15,-16,-17,-14,-18,]),'ALTER':([0,3,8,10,20,22,23,24,31,32,33,36,38,49,50,51,52,53,57,],[5,5,5,-6,-20,-19,-21,-7,-22,-23,-12,-8,-9,-13,-15,-16,-17,-14,-18,]),'DROP':([0,3,8,10,20,22,23,24,31,32,33,36,38,49,50,51,52,53,57,],[6,6,6,-6,-20,-19,-21,-7,-22,-23,-12,-8,-9,-13,-15,-16,-17,-14,-18,]),'SHOW':([0,3,8,10,20,21,22,23,24,31,32,33,36,38,49,50,51,52,53,57,],[7,7,7,-6,-20,32,-19,-21,-7,-22,-23,-12,-8,-9,-13,-15,-16,-17,-14,-18,]),'OR':([4,],[11,]),'TYPE':([4,],[13,]),'DATABASE':([4,5,6,19,],[12,15,16,30,]),'TABLE':([4,],[14,]),'DATABASES':([7,],[17,]),'REPLACE':([11,],[19,]),'IDENTIFICADOR':([12,13,14,15,16,26,30,37,40,42,43,44,47,48,55,56,58,61,],[21,21,21,25,-11,36,-50,-10,45,-52,50,50,56,-51,-48,-54,-49,-53,]),'IF':([16,30,45,],[27,41,41,]),'LIKE':([17,],[29,]),'PTCOMA':([17,28,39,45,54,55,56,58,61,],[-56,38,-55,-50,57,-48,-54,-49,-53,]),'RENAME':([25,],[34,]),'OWNER':([25,30,45,],[35,42,42,]),'EXISTS':([27,46,],[37,55,]),'CARACTER_O_CADENA':([29,],[39,]),'TO':([34,35,],[43,44,]),'NOT':([41,],[46,]),'IGUAL':([42,59,],[48,48,]),'CURRENT_USER':([43,44,],[51,51,]),'SESSION_USER':([43,44,],[52,52,]),'NOENTERO':([48,59,60,],[-51,-52,61,]),'MODE':([56,],[59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'instrucciones':([0,8,],[2,18,]),'instruccion':([0,3,8,],[3,8,3,]),'instruccionesp':([3,],[9,]),'createp':([4,],[10,]),'createpp':([12,13,14,],[20,22,23,]),'alterp':([15,],[24,]),'dropp':([16,],[26,]),'opcional3':([17,],[28,]),'createtp':([21,],[31,]),'alterpp':([25,],[33,]),'opcional':([30,45,],[40,54,]),'opcional1':([42,59,],[47,60,]),'alterppp':([43,44,],[49,53,]),'opcional2':([56,],[58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> instrucciones','s',1,'p_inicio','gramatica.py',205),
  ('instrucciones -> instruccion instruccionesp','instrucciones',2,'p_instrucciones_lista','gramatica.py',210),
  ('instrucciones -> <empty>','instrucciones',0,'p_instrucciones_lista','gramatica.py',211),
  ('instruccionesp -> instruccion instrucciones','instruccionesp',2,'p_instrucciones_lista1','gramatica.py',216),
  ('instruccionesp -> <empty>','instruccionesp',0,'p_instrucciones_lista1','gramatica.py',217),
  ('instruccion -> CREATE createp','instruccion',2,'p_instruccion_create','gramatica.py',222),
  ('instruccion -> ALTER DATABASE alterp','instruccion',3,'p_instruccion_create','gramatica.py',223),
  ('instruccion -> DROP DATABASE dropp IDENTIFICADOR','instruccion',4,'p_instruccion_create','gramatica.py',224),
  ('instruccion -> SHOW DATABASES opcional3 PTCOMA','instruccion',4,'p_instruccion_showdatabase','gramatica.py',229),
  ('dropp -> IF EXISTS','dropp',2,'p_dropprima','gramatica.py',236),
  ('dropp -> <empty>','dropp',0,'p_dropprima','gramatica.py',237),
  ('alterp -> IDENTIFICADOR alterpp','alterp',2,'p_alterprima','gramatica.py',242),
  ('alterpp -> RENAME TO alterppp','alterpp',3,'p_alterprima1','gramatica.py',247),
  ('alterpp -> OWNER TO alterppp','alterpp',3,'p_alterprima1','gramatica.py',248),
  ('alterppp -> IDENTIFICADOR','alterppp',1,'p_alterprima2','gramatica.py',253),
  ('alterppp -> CURRENT_USER','alterppp',1,'p_alterprima2','gramatica.py',254),
  ('alterppp -> SESSION_USER','alterppp',1,'p_alterprima2','gramatica.py',255),
  ('createp -> OR REPLACE DATABASE opcional IDENTIFICADOR opcional PTCOMA','createp',7,'p_createprima','gramatica.py',261),
  ('createp -> TYPE createpp','createp',2,'p_createprima','gramatica.py',262),
  ('createp -> DATABASE createpp','createp',2,'p_createprima','gramatica.py',263),
  ('createp -> TABLE createpp','createp',2,'p_createprima','gramatica.py',264),
  ('createpp -> IDENTIFICADOR createtp','createpp',2,'p_createbiprima','gramatica.py',269),
  ('createtp -> SHOW','createtp',1,'p_createtriprima','gramatica.py',274),
  ('l_campos -> IDENTIFICADOR l_campo l_campos','l_campos',3,'p_create_campos_tablas','gramatica.py',281),
  ('l_campos -> COMA IDENTIFICADOR l_campo l_campos','l_campos',4,'p_create_campos_tablas','gramatica.py',282),
  ('l_campos -> <empty>','l_campos',0,'p_create_campos_tablas','gramatica.py',283),
  ('l_campo -> tipo l_campo','l_campo',2,'p_create_campo_tabla','gramatica.py',286),
  ('l_campo -> <empty>','l_campo',0,'p_create_campo_tabla','gramatica.py',287),
  ('tipo -> INTEGER','tipo',1,'p_tipo_datos','gramatica.py',294),
  ('tipo -> DATE','tipo',1,'p_tipo_datos','gramatica.py',295),
  ('tipo -> NOT','tipo',1,'p_tipo_datos','gramatica.py',296),
  ('tipo -> NULL','tipo',1,'p_tipo_datos','gramatica.py',297),
  ('tipo -> PRIMARY KEY','tipo',2,'p_tipo_datos','gramatica.py',298),
  ('tipo -> FOREIGN KEY REFERENCES','tipo',3,'p_tipo_datos','gramatica.py',299),
  ('tipo -> CONSTRAINT','tipo',1,'p_tipo_datos','gramatica.py',300),
  ('tipo -> UNIQUE','tipo',1,'p_tipo_datos','gramatica.py',301),
  ('tipo -> IDENTIFICADOR','tipo',1,'p_tipo_datos','gramatica.py',302),
  ('tipo -> VARCHAR PARIZQ NOENTERO PARDER','tipo',4,'p_tipo_datos1','gramatica.py',308),
  ('tipo -> CHAR PARIZQ NOENTERO PARDER','tipo',4,'p_tipo_datos1','gramatica.py',309),
  ('tipo -> CHECK PARIZQ expresion PARDER','tipo',4,'p_tipo_datos1','gramatica.py',310),
  ('tipo -> DECIMAL PARIZQ NOENTERO COMA NOENTERO PARDER','tipo',6,'p_tipo_datos2','gramatica.py',316),
  ('tipo -> DOUBLE','tipo',1,'p_tipo_datos2','gramatica.py',317),
  ('tipo -> DECIMAL','tipo',1,'p_tipo_datos2','gramatica.py',318),
  ('tipo -> NOENTERO','tipo',1,'p_tipo_datos2','gramatica.py',319),
  ('l_cadenas -> PARIZQ CARACTER_O_CADENA l_cadenasp PARDER','l_cadenas',4,'p_listaCadenas','gramatica.py',328),
  ('l_cadenasp -> COMA CARACTER_O_CADENA l_cadenasp','l_cadenasp',3,'p_listaCadenas2','gramatica.py',332),
  ('l_cadenasp -> <empty>','l_cadenasp',0,'p_listaCadenas2','gramatica.py',333),
  ('opcional -> IF NOT EXISTS','opcional',3,'p_opcional','gramatica.py',340),
  ('opcional -> OWNER opcional1 IDENTIFICADOR opcional2','opcional',4,'p_opcional','gramatica.py',341),
  ('opcional -> <empty>','opcional',0,'p_opcional','gramatica.py',342),
  ('opcional1 -> IGUAL','opcional1',1,'p_opcional1','gramatica.py',346),
  ('opcional1 -> <empty>','opcional1',0,'p_opcional1','gramatica.py',347),
  ('opcional2 -> MODE opcional1 NOENTERO','opcional2',3,'p_opcional2','gramatica.py',351),
  ('opcional2 -> <empty>','opcional2',0,'p_opcional2','gramatica.py',352),
  ('opcional3 -> LIKE CARACTER_O_CADENA','opcional3',2,'p_opcional3','gramatica.py',357),
  ('opcional3 -> <empty>','opcional3',0,'p_opcional3','gramatica.py',358),
  ('expresion -> MENOS NOENTERO','expresion',2,'p_expresion_unaria','gramatica.py',368),
]
