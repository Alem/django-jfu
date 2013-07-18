import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse
from photos.models import Photo

@require_POST
def upload( request ):
    file = upload_receive( request )
    instance = Photo( file = file )
    instance.save()

    basename = os.path.basename( instance.file.file.name )
    file_dict = {
        'name' : basename,
        'size' : instance.file.file.size,

        'url': settings.MEDIA_URL + basename,
        'thumbnail_url': settings.MEDIA_URL + basename,

        'delete_url': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'delete_type': 'POST',
    }

    return UploadResponse( request, file_dict )

@require_POST
def upload_delete( request, pk ):
    success = True
    try:
        instance = Photo.objects.get( pk = pk )
        os.unlink( instance.file.file.name )
        instance.delete()
    except Photo.DoesNotExist:
        success = False

    return JFUResponse( request, success )
