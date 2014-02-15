import json
from django.http import HttpResponse


def upload_receive( request ):
    """
    Returns the file(s) uploaded by the user.
    """
    return request.FILES['files[]'] if request.FILES else None


class JFUResponse( HttpResponse ):
    """
    Returns an HTTP response with its data encoded in JSON format.

    Content-Type negotation is handled transparently for uploads using the
    Iframe Transport module through inspection of the original request object.
    """

    def __init__( self, request, data = True, *args, **kwargs ):
        data = json.dumps( data )
        j    = "application/json"
        mime = j if j in request.META['HTTP_ACCEPT_ENCODING'] else 'text/plain'
        super( JFUResponse, self ).__init__( data, mime, *args, **kwargs )
    

class UploadResponse( JFUResponse ):
    """
    Takes a dictionary containing the required jQuery File Upload fileupload
    response data and returns a JFUResponse.

    The dictionary may take the following form:
    {
       'name': 'file name', 
       'size': 12345,
       'url' : 'file url', 
       'thumbnailUrl': 'thumbnail url',
       'deleteUrl'   : 'delete url',
       'deleteType'  : 'delete type', 
    }

    Refer to the jQuery File Upload documentation for acceptable response data.
    [https://github.com/blueimp/jQuery-File-Upload/wiki/Setup]
    """

    def __init__( self, request, file_dict, *args, **kwargs ):
        files = file_dict if isinstance( file_dict, list ) else [ file_dict ]
        data  = { 'files' : files }
        super( UploadResponse, self ).__init__( request, data, *args, **kwargs )
