from flask import Blueprint, render_template, request, redirect, url_for, flash
from apps.home.model import Candidato
from database import db
from sqlalchemy import func


home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route('/')
def index():
    candidatos = Candidato.query.all()
    
    total_votos = db.session.query(func.sum(Candidato.votos)).scalar()
    
    quociente_eleitoral = total_votos // 13

    resultados = db.session.query(Candidato.partido, func.sum(Candidato.votos).label('total_votos'))\
                           .group_by(Candidato.partido).all()
    
    print(resultados)
    
    return render_template('home/index.html', 
                           candidatos=candidatos, 
                           total=total_votos, 
                           quociente_eleitoral=quociente_eleitoral, 
                           resultados=resultados)

@home_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        partido = request.form.get('partido')
        numero = request.form.get('numero')
        votos2 = request.form.get('votos')
        votos = 1

        candidato = Candidato(nome, partido, numero, votos)
        db.session.add(candidato)
        db.session.commit()

        return redirect(url_for('home_bp.cadastrar'))
    
    return render_template('home/cadastrar.html')

@home_bp.route('/candidatos')
def candidatos():    
    candidatos = Candidato.query.all()
    return render_template('home/candidatos.html', candidatos=candidatos)

@home_bp.route('/candidatos/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
    candidato = Candidato.query.get(id)
    if candidato:
        db.session.delete(candidato)
        db.session.commit()
        flash('Candidato excluído com sucesso!', 'success')
        return redirect(url_for('home_bp.candidatos'))        
    
    return render_template('home/candidatos.html')

@home_bp.route('/atualizar_candidato/<int:id>', methods=['POST'])
def atualizar_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    # Atualiza os campos conforme os valores do formulário    
    candidato.votos = request.form['votos']    
    
    db.session.commit()
    return '', 204  # Resposta vazia com código 204 (Sem conteúdo)