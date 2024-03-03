# This is a quick guide on installing the UMT testnet block producer on Mina
This is based on my excperience, I hope it helps you.



## 0. If you have installed previously the devnet version you need to remove it
```
mina client stop
sudo apt remove mina-devnet=1.0.1umt-stop-slot-992168e 
sudo mv /tmp/coda_cache_dir /tmp/coda_cache_dir_bak
sudo mv $HOME/.mina-config $HOME/.mina-config_bak   
```

#### 0.1 I had to purge, remove dependencies and celanup us as well (skip this step, you can always visit it latter if you have issues)

```
apt-get purge mina-devnet=1.0.1umt-stop-slot-992168e
apt-get autoremove
apt-get autoclean
reboot # It will reboot the system
```
## 1. Clean up, add and update repository
```
sudo rm /etc/apt/sources.list.d/mina*.list
sudo echo "deb [trusted=yes] http://packages.o1test.net $(lsb_release -cs) umt" | sudo tee /etc/apt/sources.list.d/mina.list
sudo apt-get update
```
## 2. Install Mina hardfork version
```
sudo apt-get install --allow-downgrades -y mina-devnet-hardfork=2.0.0umt-hardfork-automation-umt-eb0a6d0
```
#### 2.1 Generate libp2p keys (skip this step if you have the keys)
```
 mina libp2p generate-keypair /path/to/folder/where/to/store/filename
```

## 3. Create the service file and enviroenment file (this is the one that I was having issues with)
In the terminal type:

```
sudo nano /etc/systemd/system/mina.service
```

and paste the following:

```
[Unit]
Description=Mina Protocol
After=network.target

[Service]
User=root
EnvironmentFile=/path/to/.mina-env
ExecStart=mina daemon \
--block-producer-key /path/to/keys/my-wallet \
--config-directory /path/to/.mina-config/ \
--enable-peer-exchange true \
--external-ip Replace_this_with_your_IP \
--file-log-level Debug \
--file-log-rotations 500 \
--generate-genesis-proof true \
--insecure-rest-server \
--libp2p-keypair /path/to/folder/where/you/store/lib2pkey/filename \
--log-json \
--log-level Debug \
--log-precomputed-blocks true \
--log-snark-work-gossip true \
--metrics-port 10001 \
--node-error-url https://nodestats-itn.minaprotocol.tools/submit/stats \
--node-status-url https://nodestats-itn.minaprotocol.tools/submit/stats \
--peer-list-url https://storage.googleapis.com/o1labs-gitops-infrastructure/o1labs-umt-post-fork-run-1/seeds-o1labs-umt-post-fork-run-1.txt

Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target

```

Replace the paths on the text above that you have copied
```
EnvironmentFile=/path/to/.mina-env >>>> add the path to your .mina-env file
--block-producer-key /path/to/keys/my-wallet >>>> replace with the path to your wallet, usually it is /user/home/keys/my-wallet or /root/keys/my-wallet if you are using directly root.
--config-directory /path/to/.mina-config/ >>>> replace with the path to your .mina-config folder
--external-ip Replace_this_with_your_IP >>>>  Replace by your public IP
--libp2p-keypair /path/to/folder/where/you/store/lib2pkey/filename >>>> add the path to where you have stored your libp2p key, filename included (at least for me it was necessary)
```

after making the modifications, type ```Ctrl+x``` to close and on the prompt type ```y``` to confirm saving the file changes.

## 4. Create mina env file

```
nano .mina-env
```

copy the following inside

```
MINA_PRIVKEY_PASS="Replace_with_your_private_key_password"
UPTIME_PRIVKEY_PASS="Replace_with_your_private_key_password"
MINA_LIBP2P_PASS="Replace_with_your_libp2p_key_password"
RAYON_NUM_THREADS=6
```

Remember to replace the values with the **password** that you have received via email and the one you used to create the libp2p keys.

after making the modifications, type ```Ctrl+x``` to close and on the prompt type ```y``` to confirm saving the file changes.

## 5. Reload, enabled and run the daemon.

```
sudo systemctl daemon-reload
sudo systemctl enable mina
sudo systemctl start mina
sudo journalctl -u mina -n 1000 -f
```

The last line will show you the log, at some point you will see peers connecting from the logs. You can close the log viewing with Ctrl+C and check the satus of your node with

```
mina client status
```

After all this the node should show synced and with peers more than 0.
