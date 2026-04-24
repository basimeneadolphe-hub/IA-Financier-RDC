# On coupe la clé en deux morceaux pour que ton téléphone ne force pas le retour à la ligne
partie1 = "AIzaSyDP98nptCOu6NxOib1na6"
partie2 = "iNcZae1T2B9Ls"

# L'ordinateur colle les deux morceaux tout seul
cle_complete = partie1 + partie2
genai.configure(api_key=cle_complete)
