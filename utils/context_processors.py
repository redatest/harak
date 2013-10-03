from app.models import New


def info(request):
	return {
	'last_info': New.objects.all()[:4],
	#'site_name': settings.SITE_NAME,
	#'meta_keywords': settings.META_KEYWORDS,
	#'meta_description': settings.META_DESCRIPTION,
	'request': request
	}
