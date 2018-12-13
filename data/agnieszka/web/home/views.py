

from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect

from home.models import Website


class HomeView(TemplateView):
    template_name = "agnieszka/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if "lucky" in self.request.GET.keys():
            results = context.get('results', [])

            if results:
                try:
                    res = results.pop(0)
                    return HttpResponseRedirect(redirect_to=res.url)
                except IndexError:
                    pass

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        query = self.request.GET.get("query", None)

        context["no_query"] = False

        if query is not None:
            links_qs = Website.objects.filter(url__contains=query)
            titles_qs = Website.objects.filter(meta_title__contains=query)
            descr_qs = Website.objects.filter(meta_description__contains=query)

            qs = []

            qs.extend([x for x in links_qs])
            qs.extend([x for x in titles_qs])
            qs.extend([x for x in descr_qs])

            context['results'] = qs
            context['query'] = query
        else:
            context["no_query"] = True

        return context
