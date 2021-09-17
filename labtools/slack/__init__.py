"""
Tools for cleaning and managing slack exports because i will be god damned if we reward them for repackaging and displacing IRC.

Exporting Slack Data
---------------------

Following the `slack docs <https://slack.com/help/articles/201658943-Export-your-workspace-data>`_ ...


- From your desktop, click your workspace name in the top left.
- Select Settings & administration from the menu, then click Workspace settings.
- Click Import/Export Data in the top right.
- Select the Export tab.
- Below Export date range, open the drop-down menu to select an option.
- Click Start Export. We'll send you an email once your export file is ready.
- Open the email and click Visit your workspace's export page.
- Click Ready for download to access the zip file.


Archiving Slack Data
--------------------

Slack will export a big messy collection of .json files. To make them ready for archive, we

- download all the file attachments with :func:`~.slack.load.download_attachments` , and
- clean the extraneous information with :func:`~.slack.load.clean_messages`

These are both wrapped with :func:`~.slack.load.load_messages` .

So after unzipping the folder from the previous step, call ``load_messages`` with the full directory as its only argument, and
get a dataframe of cleaned messages back::

    >>> df = load_messages('slack/backup/dir')
    >>> df.head()

          channel                  timestamp display_name    real_name                               files                                               text
    1050  general 2021-01-25 11:42:52.016700        Jonny        Jonny                                  []  what a lovely week to FREAKING SHRED on whatev...
    1051  general 2021-01-25 11:43:10.016800        Jonny        Jonny                                  []                        GOOD LUCK, AND GET SHREDDIN
    1052  general 2021-01-25 22:51:22.017000        Jonny        Jonny                                  []  (or get self-caring that is also valid, in tha...
    1053  general 2020-07-09 13:06:54.015700    mike wehr    mike wehr                                  []  Hi All, here is a draft of the Prey Capture gr...
    1054  general 2020-07-09 22:17:12.015800          Kat          Kat                                  []  I'll have to tell Rhythm! He asks about it all...
    1055  general 2020-10-21 12:28:41.023500         None         None       [F01CZ902153___Snap-4187.jpg]  Totally frivolous, non-scientific question her...
    1056  general 2020-10-21 12:31:47.023900         None         None           [F01CVKX1QGN___image.png]                                           fixed it
    1057  general 2020-10-21 12:36:47.024200         None         None  [F01DS7RE74Y___Image from iOS.jpg]
    1058  general 2020-10-21 12:37:50.025500  aldisweible  aldisweible                                  []  Not what I was thinking, but a good vote. I'm ...
    1059  general 2020-10-21 14:21:32.025700        Jonny        Jonny                                  []                                  fucking nailed it

you can then save the dataframe using normal means like ``df.to_json()`` etc.

The files produced by ``download_attachments`` are by default downloaded to a ``files`` subdirectory beneath the ``base_dir``,
so make sure you save those too!
"""

from labtools.slack.load import load_messages