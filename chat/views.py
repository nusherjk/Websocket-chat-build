from django.shortcuts import render
from django.views.generic import TemplateView



class Landing(TemplateView):
    template_name = 'chat/index.html'


class Room(TemplateView):
    template_name = 'chat/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = kwargs['room_name']
        return context


