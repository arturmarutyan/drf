from rest_framework.authentication import TokenAuthentication as BaseToken

class TokenAuthentication(BaseToken):
    '''
    До этого нужно было писать Token f{}, теперь Bearer
    '''
    keyword = 'Bearer'