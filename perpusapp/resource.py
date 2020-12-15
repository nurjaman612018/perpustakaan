from import_export import resources
from perpusapp.models import Buku

class BukuResource(resources.ModelResource):
    class Meta:
        model = Buku
