---
layout: page
---
[//]: <>

Plonkiči, ki mi pridejo prav..

### Git
'git init <dir>' -> creates empty repo in <dir>
'git clone <repo>' -> clones repo to local machine
'git add <dir>' -> stage all changes in <dir> for next commit. Change <dir> with <file> for a specific file
'git commit -m "<message>"' -> commit the staged snapshot
'git status' -> list of files that are staged, unstaged and untracked
'git push <remote> <branch>' -> push the branch to <remote>

Da postaviš 'remote', potrebuješ le oddaljen disk, kjer je mapa, ki ima '.git'. Nato daš ukaz 'git init  --bare'.

Ideja -> git kot backup za datoteke

### Python

#### Plotting
širši graf: 'plt.figure(figsize=(20,5))'

ekstremi: 'from scipy.signal import argrelextrema'
'c=argrelextrema(b, np.less, order=30)'
c -> seznam indeksov
np.less -> minimum funkcije
np. greater -> maksimum funkcije
order -> kriterij filtriranja

### Jekyll
Lokalni zagon: 'jekyll serve'

### Mreža

#### Dostop do Win diska iz Maca in Linuxa
Win: Folder -> properties -> advance sharing -> share this folder
Permissions -> add -> advanced -> find now -> auth.users

Admin tools -> Computer management -> local users and groups -> users -> desna miškina tipka -> New user -> vnesi uporabniško ime in geslo

Control Panel -> network connections -> properties -> IPv4 -> properties -> use the following IPv4

Mac: Finder -> Go -> Connect to server -> smb://<server ip> -> vnesi uporabniško ime in geslo

