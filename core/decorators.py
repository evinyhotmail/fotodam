from django.shortcuts import render, redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs) :
        if request.user.is_authenticated:
            # I just sent  to redirect function the pk 
            # when the user is already athenticated 
            # in order to call Dashboard view with the last Condominium used
            return redirect ( 'core:dashboard' )
        else :
            return view_func ( request, *args, **kwargs )

    return wrapper_func



