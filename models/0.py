# coding: utf8
# coding: utf8
db = DAL('sqlite://storage.sqlite')
e_m  = {
        'empty':'Este campo é obrigatório',
        'in_db':'Este registro já existe no banco de dados',
        'not_in_db':'Este registro não existe no banco de dados',
        'email':'Você precisa inserir um e-mail válido',
        'image':'O arquivo precisa ser uma imagem válida',
        'not_in_set':'Você precisa escolher um valor válido',
        'not_in_range':'Digite um número entre %(min)s e %(max)s',
       }
            
config = dict(nmsite='IguassuPass',dscsite='Tickets on-line')

