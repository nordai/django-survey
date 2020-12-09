# -*- coding: utf-8 -*-

from django import forms


class ImageSelectWidget(forms.widgets.Widget):
    template_name = "survey/forms/image_select.html"
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js",
            "http://maps.googleapis.com/maps/api/js?sensor=false",
            "js/survey.js",
        )

    def get_context(self, name, value, attrs):

        choices = []
        for index, choice in enumerate(self.choices):
            print (choice[0])
            if choice[0] != "":
                title, img_src = choice[1].split(":", 1)
                choices.append({"img_src": img_src, "value": choice[0], "title": title, "index": index})

        return {'widget': {
            'name': name,
            'value': value,
            'attrs': attrs,
            'choices': choices
        }}
