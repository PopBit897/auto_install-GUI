echo "choose ip_tools or ip_tools_GUI"
echo "1=ip_tools_GUI"
echo "2=ip_tools for cmd and teminal linux,Mac"
read i
condizione=1
condizione2=2
if  [ $i = $condizione ];then 
    git clone https://github.com/RedAnonymusITA/ip_tools_GUI.git

    cd ip_tools_GUI

    sudo chmod a+x open_for_linux.sh

    ./open_for_linux.sh
elif [ $i=$condizione2 ];then
    git clone https://github.com/RedAnonymusITA/ip-tools.git

    cd ip-tools
    cd ip

    sudo chmod a+x start.sh

    ./start.sh
     
fi
