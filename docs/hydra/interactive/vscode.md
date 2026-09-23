# VS Code

There are several ways to use VSCode with and on Hydra, you can either


1. run VSCode on your local machine and ssh to a login node, or
2. run VSCode on Hydra, or
3. start a VSCode server on Hydra, or
4. start a VSCode tunnel on Hydra.


## Which version to use?


These are all available and acceptable options, although some have limitations and/or quirks, starting a VSCode server is the recommended method.


- Running VSCode on your local machine and ssh to a login node is the simplest way to use VSCode.
    - but, the counterpart program (client) will run on the login node and it may get reniced or even killed if it uses a lot of resource,
    - there is no way to use an interactive node as client.
- Running VSCode on Hydra is possible, but it only makes sense if you have a very fast connection since
    - it displays its output on your local machine using the X-Windows protocol
        - it can be slow and your local machine must support X (via a X server), and
        - your connection must allow X tunneling.
    - Not all X servers support this method
    - Moreover,even if you `qlogin` to an interactive node, it may not work (it is a virtual memory hog).
- Starting a VSCode server on Hydra is the best way to do this and you can use an interactive node as server.
    - You will need to start a ssh tunnel on your local machine and
    - will use VSCode inside a browser on your local machine.
- Starting a VSCode tunnel on Hydra is possible, as long as you use GitHub for authentication, and you can use an interactive node.
    - No need to start a ssh tunnel on your local machine, but starting the tunnel fails from time to time (you just restart it) and
    - you need GitHub credentials (using you SI Microsoft credentials fails because of SI MFA implementation).
    - You will use VSCode inside a browser on your local machine.


## HowTo


### 1- Use VSCode on your local machine and ssh to a login node


- Install `vscode` on your machine and the `Remote-SSH` extension.
- Using the `Connect to Host,` use `vscode` to ssh to one of the login nodes, using your Hydra credentials.


### 2- Use VSCode on Hydra


- ssh to a login node, enable X-tunneling
- load the `tools/vscode` module
- run `vscode-desktop --no-sandbox --disable-gpu`
    - ``does not work with all X-servers
        - works with Linux/X11, MacOS/xquartz, Windows/Cygwin/X
        - fails with Windows/xming
        - problems with `rdp` to a Linux/X11 server
- Using an interactive node via `qlogin` might not work because of very high virtual memory usage.


### 3- Start a VSCode Server


- ssh to a login node,
- `qrsh` to an interactive node,
- load the `tools/vscode` module,
- run `start-vscode-server` to start the server and follow the instructions,
    - use `start-vscode-server -help` to see all the options,
    - the ssh tunnel must be run in a terminal window on your local machine,
    - point your browser to the correct URL, the one with `localhost` in it, not the IP number of the client host.


#### Example


1. Start the server on an interactive node


```{.text title="On a login node"}
sylvain@login01% qrsh

sylvain@compute-64-15% module load tools/vscode
sylvain@compute-64-15% start-vscode-server
start-vscode-server: starting vscode server on host=compute-64-15 IP=192.168.92.85 and port=8000
  you need to create a ssh tunnel on your local machine with
    ssh -N -L 8000:192.168.92.85:8000 sylvain@hydra-login01.si.edu
  in a terminal window.

Next, point your browser to the URL http://localhost:8000?tkn=XXX on your local machine, you will find the token below,
  but not the URL with 192.168.92.85 listed below !!!

Use Control+C in this window to kill the server when done.

Hit ENTER to continue and start the server ...
  wait for the server to start...
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
Web UI available at http://192.168.92.85:8000?tkn=6031bf1b-25cd-4d43-96b1-e02bd3dfa5f3
```


- the token - `6031bf1b-25cd-4d43-96b1-e02bd3dfa5f3` - will be a different one each time, unless
    - you use the option `-no-token,`or
    - select yourself a token with the option `-token TTTT` where `TTTT` is the token you want to use (any string will do)
- use the option `-help` to see all the options.


2. Start the ssh tunnel on your local machine


```{.text title="On your local machine, in a terminal window"}
ssh -N -L 8000:192.168.92.85:8000 sylvain@hydra-login01.si.edu
```


- the IP and port numbers - the string `8000:192.168.92.85:8000` - are likely to be different, and
    - replace `sylvain` by your username on Hydra.


3. Start a browser on your local machine and go to (use the right token)


`http://localhost:8000?tkn=6031bf1b-25cd-4d43-96b1-e02bd3dfa5f3`


and you should get VSCode running:


![](../../assets/vscode-server.jpg)


You will be asked to choose things the first time you start it.


### 4- Start a VSCode Tunnel


- ssh to a login node,
- `qrsh` to an interactive node,
- load the `tools/vscode` module,
- run `start-vscode-tunnel`to create the tunnel and follow the instructions,
    - use `start-scode-tunnel -help` to see all the options,
    - use your GitHub credentials, not SI Microsoft ones (you may need to register with GitHub to get these),
    - point your browser to the `https://vscode.dev/tunnel/xxx` URL, where `xxx` is the tunnel name,
    - select 'Use GitHub' in the browser if asked which authentication to use when connecting,
    - restart the tunnel if it fails on a `dns error` ,
        - you can use `host <hostname>`to resolve the hostname listed in the URL of error message, this should return an IP number.


#### Example


1. Start the server on an interactive node


```{.text title="On a login node"}
sylvain@login01% qrsh

sylvain@compute-64-15% module load tools/vscode
sylvain@compute-64-15% start-vscode-tunnel
start-vscode-tunnel: starting a tunnel, name: sylvain-compute-64-15

  to access the tunnel, point your browser to https://vscode.dev/tunnel/sylvain-compute-64-15 on your local machine.
  to reset your credentials, delete the '/home/sylvain/.vscode/cli/token.json' file.

Use Control+C in this window to kill the tunnel when done.

Hit ENTER to continue and start the tunnel ...
  wait for the tunnel to start...
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
? How would you like to log in to Visual Studio Code? ›
   Microsoft Account
[] GitHub Account
To grant access to the server, please log into https://github.com/login/device and use code ABE4-F1A6
```


- be sure to select `GitHub Account` (using up/down arrows), then hit ENTER
    - you will get a different code than `ABE4-F1A6,`
    - use your browser to grant access


```{.text title="You may next see"}
...
[2024-07-09 18:28:20] error failed to lookup tunnel: connection error: error sending request for url (https://use.rel.tunnels.api.visualstudio.com/tunnels/tidy-chair-cx8htn2?includePorts=true&tokenScopes=host&api-version=2023-09-27-preview): error trying to connect: dns error: failed to lookup address information: Try again
```


In this case, simply restart as follows:


- resolve the host name, and
- restart the tunnel:


```
sylvain@compute-64-15% host use.rel.tunnels.api.visualstudio.com
use.rel.tunnels.api.visualstudio.com is an alias for tunnels-prod-rel-use-live-tm.trafficmanager.net.
tunnels-prod-rel-use-live-tm.trafficmanager.net is an alias for v3-use.cluster.rel.tunnels.api.visualstudio.com.
v3-use.cluster.rel.tunnels.api.visualstudio.com is an alias for tunnels-prod-rel-use-v3-cluster.eastus.cloudapp.azure.com.
tunnels-prod-rel-use-v3-cluster.eastus.cloudapp.azure.com has address 20.120.56.11

sylvain@compute-64-15% start-vscode-tunnel
start-vscode-tunnel: starting a tunnel, name: sylvain-compute-64-15

  to access the tunnel, point your browser to https://vscode.dev/tunnel/sylvain-compute-64-15 on your local machine.
  to reset your credentials, delete the '/home/sylvain/.vscode/cli/token.json' file.

Use Control+C in this window to kill the tunnel when done.

Hit ENTER to continue and start the tunnel ...
  wait for the tunnel to start...
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*

Open this link in your browser https://vscode.dev/tunnel/sylvain-compute-64-15
```


3. Start a browser on your local machine and go to the given URL, something like


`https://vscode.dev/tunnel/sylvain-compute-64-15`


but will be different in your case, and you should get VSCode running via a tunnel:


![](../../assets/vscode-tunnel.jpg)


### Notes


You could run either, the server or the tunnel, on a login node but we *strongly recommend* that you use instead an interactive node:


- processes running on a login node for a long time and consuming resources get slowed down and eventually killed, hence your VSCode might die before you're done.


There are resource limits on interactive sessions, tho,


Check the relevant documentation regarding the [Interactive Queue](../jobs/queues.md) under [Available Queues](../jobs/queues.md).


**Also**


```{.text title="You can use a convenient script as follows"}
module load tools/vscode
start-vscode
Which VSCode: desktop, server or tunnel?
```


type in d, desktop, s, server, t, or tunnel to start either.


