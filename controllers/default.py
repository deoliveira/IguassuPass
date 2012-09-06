# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    response.flash = "Welcome to web2py!"
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

def getstarted():
 
    return (dict(message=T('GetStarted')))

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def atracoes():
    #atracoes = db(db.atracao).select(orderby=db.atracao.nome)
    multimedias = db(db.multimedia).select(orderby=db.multimedia.id)
    #multimedias = db(db.multimedia.atracao == atracoes).select(orderby= db.multimedia.id)
    return locals()

@auth.requires_login()
def atracao_create():
    form= crud.create(db.atracao, next='atracoes')
    return locals()

@auth.requires_login()
def atracao_edit():
    atracao = db.atracao(request.args(0)) or redirect(URL('atracoes'))
    form = crud.update(db.atracao, atracao, next='atracoes')
    return locals()

@auth.requires_login()
def multimedia_create():
    #db.multimedia.atracao.default = request.args(0)
    form = crud.create(db.multimedia)
    return locals()

@auth.requires_login()
def multimedia_edit():
    #multimedia = db.multimedia(request.args(0)) or redirect(URL('atracoes'))
    form = crud.update(db.multimedia, multimedia)
    return locals()

def customersfeedback():
    #feedback = db.comment(request.args(0)) or redirect(URL('index'))
    #if auth.user:
    #    db.comment.posted_on.default = request.now
    #    db.comment.posted_by.default = auth.user.id
    #    form = crud.create(db.comment)
    #comments = db(db.comment).select(orderby=db.comment.posted_on)
    return locals()