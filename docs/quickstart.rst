Quickstart
==========

Setting up Lavalink server
--------------------------
Download the latest `Lavalink.jar <https://github.com/freyacodes/Lavalink/releases/>`_
Place an ``application.yml`` file in the same directory. The file should look like `this <https://github.com/freyacodes/Lavalink/blob/master/LavalinkServer/application.yml.example/>`_.

Run ``java -jar Lavalink.jar`` in the directory of the jar.

Using Lavalink.py
-----------------
This only applies if you are using the library `nextcord <https://github.com/nextcord/nextcord/>`_ and with `Lavalink v3.1+ <https://github.com/freyacodes/Lavalink/releases/>`_
Although backwards compatibility may be possible, it's not encouraged nor is support guaranteed.

Place the `example cog <https://github.com/Devoxin/Lavalink.py/blob/master/examples/music.py>`_ in your cogs folder or anywhere in your bot's file directory.
To add the cog you will need to add this line to your main bot file.

.. code-block:: python

    Bot.add_cog('directory.music')
