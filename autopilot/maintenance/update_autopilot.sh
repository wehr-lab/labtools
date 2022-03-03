echo "Updating Terminal Autopilot Version"
git -C /home/lab/git/autopilot pull
git -C /home/lab/autopilot/plugins/wehrlab pull
echo "Update Successful"

echo "Updating Pis"
parallel-ssh -h /home/lab/pi_ips.txt \
  -e /home/lab/autopilot_update_errors \
  -o /home/lab/autopilot_update_stdout \
  -I < /home/lab/update_pis.sh


echo "For changes on Pilots to take effect, restart them (with parallel-ssh -h ~/pi_ips.txt \"sudo restart\""
