# Eisen-tickets

<p align="center">
    <img src="assets/large-logo.PNG" alt="eisen-tickets logo">
</p>


[![GitHub pull-requests](https://img.shields.io/github/issues-pr/dat-adi/eisen-tickets.svg?style=for-the-badge&logo=appveyor)](https://github.com/dat-adi/eisen-tickets/pulls)
[![GitHub issues](https://img.shields.io/github/issues/dat-adi/eisen-tickets.svg?style=for-the-badge&logo=appveyor)](https://github.com/dat-adi/eisen-tickets/issues)
[![GitHub license](https://img.shields.io/github/license/dat-adi/eisen-tickets.svg?style=for-the-badge&logo=appveyor)](https://github.com/dat-adi/eisen-tickets/blob/master/LICENSE)
[![GitHub repo size](https://img.shields.io/github/repo-size/dat-adi/eisen-tickets.svg?style=for-the-badge&logo=appveyor)](https://github.com/dat-adi/eisen-tickets)
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=for-the-badge&logo=appveyor)](https://github.com/dat-adi/eisen-tickets/blob/master/CODE_OF_CONDUCT.md)

---

## What the Eisen-tickets is all about.
An implementation of the famous Eisenhower Box, where the 2x2 matrix defines
the priority and the status of the task at hand.

Having two categories, Urgency and Importance mixed, enables you to get a clearer
understanding of which task to invest more time into.

## Installation
The Eisen tickets can easily be brought into your system, just by simply downloading one of the [releases](https://github.com/dat-adi/eisen-tickets/releases) or by cloning the repository,
```shell
git clone https://github.com/dat-adi/eisen-tickets.git
```

## How Eisen's Tickets works
The Eisen tickets works on the principle of a ticket based system, where each ticket has it's own 
information, the time it was made, the category it belongs to in the eisenhower box, along with the task and it's contents.

### Adding a ticket into the database
Adding a ticket into the database is currently only supported in a command line format for now, and the GUI component is still underway.\
However, it is pretty simple to add a ticket into the database as well.\
Simply, go into the **src** folder and click on **main.py**, this will lead you to a command line interface.\
The process is pretty simple to undergo, and needs you to simply enter the option 2 to add tickets into the database.

Following each prompt and entering the required info helps you to essentially finish the task with close to no errors.
In case, you do make an error, we will be releasing a release in which you can delete your tickets as well.

### Displaying the tickets entered
The Eisen's Tickets, has both a GUI and a CLI feature leaving to the user to choose which mode to use.

#### GUI
The GUI feature of the Eisen's Tickets, can simply be utilized by directing yourself to the display_tickets.py in the modules folder, to display the tickets and, the adding_tickets.py to add tickets into the database, and the rest of it is pretty evident, directing and leading you to see all the displayed tickets based on your selection.

#### CLI
The CLI feature can pretty much be accessed by the **main.py** file, and simply progressing through a selection of options, allows you to view and add tickets to the database as well.

## Contributing to eisen-tickets
If you feel like there could be an improvement or a bug fix, that can be placed for the current status of the repository,
feel free to browse through the [CONTRIBUTING.md](https://github.com/dat-adi/eisen-tickets/blob/master/CONTRIBUTING.md) in order to realise how to proceed with your contribution.

Consider looking into the [Wiki](https://github.com/dat-adi/eisen-tickets/wiki) for Eisen's Tickets as well. It is updated from time to time, and explains the working of Eisen's Tickets and the components it uses.

---
<p align="right"><i>dat-adi</i></p>
