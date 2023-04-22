import subprocess

meta_donnees = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
donnes = meta_donnees.decode('utf-8', errors="backslashreplace")
donnes = donnes.split('\n')
profils = []
for x in donnes:
    if "All User profile" in x:
        x = x.split(':')
        x = x[1]
        x = x[1:-1]
        profils.append(x)
print("{:<30}| {:<}".format("nom du wifi", "mot de passe"))
print("--------------------------------------------------")
for x in profils:
    try:
        resultats = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', x, 'key = clear'])
        resultats = resultats.decode('utf-8', errors="backslashreplace")
        resultats = resultats.split('\n')

        resultats = [b.split(":")[1][1:-1]
                     for b in resultats if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(x, resultats[0]))

        except IndexError:
            print("{:<30}| {:<}".format(x, ""))

    except subprocess.CalledProcessError:
        print("Encoding Error Occured")
