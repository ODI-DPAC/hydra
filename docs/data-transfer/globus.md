# Globus

[Globus](https://www.globus.org/) is a service for moving data between storage systems. You set a transfer up in a web browser, and Globus runs it for you. It retries after network failures, checks that every file arrived intact, and emails you when it is done. Nothing has to stay logged in while it runs. We recommend it for transfers of hundreds of gigabytes, for data at another institution, and for any transfer that has to survive a closed laptop.

More in-depth instructions for using Globus beyond Hydra are available at <https://smithsonian.github.io/globus-docs/>. Here you sign in with your SI account, find the Hydra collections, and run a transfer.

Four terms come up in every step.

| Term | Meaning |
|---|---|
| **Collection** | A storage system that Globus can reach, with a name you search for. Hydra's are `SI_hydra_scratch` and the others listed below. |
| **Endpoint** | The computer that serves a collection. Hydra's endpoints are `hydra-globus01` and `hydra-globus02`. You never address them directly. |
| **Globus Connect Personal** | A program that turns your own computer into a collection, so you can transfer to and from it. |
| **Transfer** | A copy between two collections that Globus runs for you. |

## Sign in

1. Open [app.globus.org](https://app.globus.org) and choose **Smithsonian Institution** as your organization:

    ![The Globus sign-in page with the organization menu](../assets/globus_CI_logon.png)

2. Sign in on the Smithsonian page with your SI network username and password. The username is the part of your email address before `@si.edu`. This is your SI account. It is separate from your Hydra account:

    ![The Smithsonian Institution sign-in page](../assets/SI_CILogon.png)

3. The first time, Globus asks whether you have an existing Globus account to link. If you do not, choose **Continue** and complete the sign-up:

    ![The first-login page asking whether to link an existing Globus account](../assets/welcome.png)

4. Allow the Globus web app to manage data on your behalf when it asks:

    ![The consent page listing what the Globus web app will do](../assets/consent.png)

## Open your Hydra directory

1. In the File Manager, type `Smithsonian` in the **Collection** search box:

    ![The Collection search box with Smithsonian typed in](../assets/collection_search.png)

    The Hydra collections begin with `SI_hydra_`:

    ![The three SI_hydra collections in a search result](../assets/si_colls.png)

    | Collection | Path on Hydra |
    |---|---|
    | `SI_hydra_scratch` | `/scratch` |
    | `SI_hydra_scratch_SAO` | `/scratch`, the SAO project partitions |
    | `SI_hydra_store/public` | `/store/public` |

2. The first time you open a collection, Globus asks you to allow access to it:

    ![The File Manager asking for consent to access a collection](../assets/auth.png)

3. Navigate to your directory, for example `/scratch/genomics/USERNAME`:

    ![The File Manager showing a directory under /scratch](../assets/scratch.png)

Globus sees files with the same permissions as your Hydra account. What you cannot read on a login node, you cannot read here either.

## Transfer

1. With your Hydra directory open in one pane, switch the File Manager to two panes. The layout buttons are at the top right. The middle one gives two panes:

    ![The File Manager in two-pane view, ready for a second collection](../assets/panel.png)

2. In the second pane, open the other collection. That can be another institution's collection, your own computer through Globus Connect Personal, or the `Globus Tutorial Endpoint` collections if you want to try a transfer with nothing at stake.

3. Select files or directories in the source pane and click **Start**. The arrow on the button shows which way the transfer goes:

    ![Files selected in the right pane, ready to transfer to the Hydra collection on the left](../assets/transfer.png)

    Globus confirms the request at the top of the page:

    ![The transfer request submitted notice](../assets/submitted.png)

4. Follow the transfer under **Activity** in the left bar. Globus emails you when it finishes, and also if it fails:

    ![The Activity page listing a completed transfer](../assets/activity.png)

## Transfer to and from your own computer

Your computer becomes a collection when it runs Globus Connect Personal. On a machine you administer, install it from Globus's instructions for [macOS](https://docs.globus.org/how-to/globus-connect-personal-mac), [Windows](https://docs.globus.org/how-to/globus-connect-personal-windows) or [Linux](https://docs.globus.org/how-to/globus-connect-personal-linux). On a Smithsonian-administered machine, install it from Software Center. Once it is running, your computer appears in the collection search under the name you gave it, and transfers work as above.

## Further reading

- [Smithsonian Globus documentation](https://smithsonian.github.io/globus-docs/) for sharing, group access and everything beyond Hydra
- [Globus documentation](https://docs.globus.org/) from Globus itself
- [Filesystems](../storage/filesystems.md) for where to put the data once it arrives
