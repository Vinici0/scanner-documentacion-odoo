Script de instalación de Odoo 13 en Ubuntu 20.04
	- Se muestra paso a paso la instalación y se recomienda seguirla e ir entendiendo el proceso seguido.
	- Se predispone al usuario con conocimientos básicos de Linux/Ubuntu
	- Se solucionan posibles errores que han surgido durante la grabación de la instalación del vídeo de la Clase I. Si se os da algún otro error podeis hacer la consulta en el foro de este curso o emplear un foro externo a fin de resolver tal incidencia.

1) sudo apt install git npm python3-pip postgresql postgresql-client-common libxml2-dev libxslt1-dev lib32z1-dev libldap2-dev libsasl2-dev libjpeg8-dev

2) Descargamos los archivos wkhtmltox y libpng12-0. Se pueden descargar a través del comando wget (o con apt-get, si no nos da error)
	sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb
	sudo wget http://archive.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb

3) sudo apt-get install xfonts-75dpi (si da error, ejecutad sudo apt --fix-broken install)
4) sudo dpkg -i *.deb #Instalamos los paquetes descargados (si da error, paso 5, sino paso 6)

5) sudo wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb
   sudo dpkg -i libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb

   sudo add-apt-repository ppa:linuxuprising/libpng12 
   sudo apt update 
   sudo apt install libpng12-0

6) sudo npm install -g less less-plugin-clean-css
7) sudo su - postgres # Configuracion del usuario de BD PostgreSQL
   createuser root -s
   psql template1
   alter role root with password 'odoo';
   \q
   exit 
 
8) sudo mkdir odoo # Creamos el directorio odoo en la ruta donde vamos a hacer la instalación (típicamente opt/odoo ó /home/odoo)
   cd odoo
   git clone https://github.com/odoo/odoo.git --branch 13.0 --single-branch --depth 1
9) cd odoo/
10)sudo pip3 install -r requirements.txt # si da errores el paquete psycho ejecutamos sudo apt-get install --reinstall libpq-dev
11)cd doc/
12)sudo pip3 install -r requirements.txt 
13)sudo ./odoo-bin -c odoo.conf -d datatest -i base
