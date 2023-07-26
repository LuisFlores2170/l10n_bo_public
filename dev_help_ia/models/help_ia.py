# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, http
from odoo.http import request
from odoo.exceptions import UserError
import json 
from odoo.addons.web.controllers.main import View


import openai

# Configura tu clave de API de OpenAI



class help_ia(models.Model):
    _name = 'help.ia'
    _description = 'module developed for consults from ia'

    
    name = fields.Char(
        string='IA',
        default='IA',
        readonly=True
        
    )

    user_id = fields.Many2one(
        string='Usuario',
        comodel_name='res.users',
        ondelete='restrict',
    )

        
    
    query_text = fields.Char(
        string='Consultar',
        help='Ingrese su consulta'
    )
    
    
    
    
    query_response = fields.Html(
        string='Respuesta',
    )
    

    def generate_query(self):
        api = self.env['ir.config_parameter'].sudo().get_param('dev_help_ia.api_key')
        
        openai.api_key = api
        # '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'
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=self.query_text,
            max_tokens=500,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=15
        )

        for record in self:
            record.query_response = str(response.choices[0].text.strip()) 

        data = self.my_route()
            
    
    
    # [AL CREAR]
    @api.constrains("create_date")
    def _constrains_name(self):
        prefix = '00000'
        self.name = "AYUDA NRO: "+prefix[:len(prefix)-len(str(self.id))]+str(self.id)


    def get_copy_html(self) -> str:
        copiar_html_script = """
            document.addEventListener("DOMContentLoaded", function() {
                var copyButton = document.getElementById('id_html');
                copyButton.click();
            });
        """

        data = {
            'mensaje': 'Hola desde JSON',
            'valor': 123
        }
        #return http.Response('dev_help_ia.nombre_plantilla', headers={'Content-Type': 'application/json'})
        return False

    def my_route(self):
        self.run_js('alert("Hola desde JavaScript");')
        return "Código JavaScript ejecutado"


"""

class MyController(http.Controller):
    @http.route('../report/script.xml', type='http', auth='public')
    def my_route(self):
        return request.render('dev_help_ia.nombre_plantilla')



"""

class MyController(View):
    @http.route(type='http', auth='public')
    def my_route(self):
        self.run_js('alert("Hola desde JavaScript");')
        return "Código JavaScript ejecutado"


