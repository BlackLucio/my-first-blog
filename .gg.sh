#!bin/bash
echo $DISPLAY
export DISPLAY=:0.0
echo $DISPLAY

xinput --list
echo "Ingrese una id"
read ID

echo "Desactivado"
xinput set-int-prop $ID "Device Enabled" 8 0

echo "Desea detenerse [Y/N]"
read respuesta

if [ $respuesta == "Y" ]  || [ $respuesta == "y" ]
then
echo "Activado"
xinput set-int-prop $ID "Device Enabled" 8 1 
else 
echo "Continua"
fi
