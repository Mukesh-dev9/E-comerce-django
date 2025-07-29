class Cart():

    def __init__(self,request):
        self.session = request.session

        #Get the current session key if it exists
        cart =self.session.get('session_key')

        #create new session key if user is new
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}
        
        #make sure cart is avilable on all pages of site
        self.cart=cart