import os


def root_context_processor(request):
    context = {}

    ga_tracking_id = os.environ.get('GA_TRACKING_ID')
    context['ga_tracking_id'] = ga_tracking_id
    if ga_tracking_id and len(ga_tracking_id) < 5:
        context['ga_tracking_id'] = None

    return context
