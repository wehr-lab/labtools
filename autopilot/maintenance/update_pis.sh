echo "---------------------------"
echo $(date)
echo "---------------------------"


git -C ~/git/autopilot pull
git -C ~/autopilot/plugins/wehrlab pull

echo "updated git repos"
echo "current autopilot version"
echo $(git -C ~/git/autopilot describe)
echo "current autopilot branch"
echo $(git -C ~/git/autopilot rev-parse --abbrev-ref HEAD)

# update timezone
sudo raspi-config nonint do_change_timezone US/Pacific

echo "updated timezone"
