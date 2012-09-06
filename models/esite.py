# coding: utf8
# coding: utf8
# coding: utf8

# criamos um validador pré definido
notempty=IS_NOT_EMPTY(error_message=e_m['empty'])

# definição da tabela de atracao
db.define_table('atracao',
                Field('nome', unique=True, notnull=True),
                Field('desc','text'),
                format='%(nome)s'
                )
                
# validadores da tabela de marcas
db.atracao.nome.requires=[notempty, IS_NOT_IN_DB(db, 'atracao.nome',error_message=e_m['in_db'])]
                                               
                                               


# definição da tabela de multimedia, podendo ser foto ou video
db.define_table('multimedia',
                Field('atracao', db.atracao, notnull=True),
                Field('src', 'list:string'),
                format='%(atracao)s - %(src)s'
                )

# validação da tabela multimedia
db.multimedia.atracao.requires=IS_IN_DB(db, 'atracao.id','atracao.nome',error_message=e_m['not_in_db']) 

#definição da tabela de comentarios

db.define_table('comment',
                Field('body', 'text', notnull=True),
                Field('posted_on', 'datetime', readable=False, writable=False),
		Field('posted_by', 'reference auth_user', readable=False, writable=False))