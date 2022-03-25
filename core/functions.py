import os
from django.conf import settings
from django.core.exceptions import ValidationError

#Fuction to return the list of categories selected 
# when the user is adding a image
def getImageCategories(post):
    qs = post.getlist('categories')
    if not qs:
        return []
    else:
        return qs


# Delete files into the directly
def DeleteFile(path) :
    filename = os.path.basename(str(path)) 
        
    destination_path = f"{settings.MEDIA_ROOT}/"
    
    if os.path.exists ( destination_path + str ( path ) ) :
        try :
            os.remove ( destination_path + str ( path ) )
            return (True, str ( path ) )
        except(
                ValidationError,
                PermissionError, 
                TypeError, 
                ValueError, 
                OverflowError,
                PermissionError) :
            return (False,  filename)
    else :
        return (False, filename)
   

