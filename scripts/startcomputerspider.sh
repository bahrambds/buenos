source ~/buenos/venv/bin/activate && cd ~/buenos/espapis && python tech_computerhoy.py  && cd ~/buenos/spiderbuenos/spiderbuenos && scrapy crawl computer -o temp/computer.json && python computerpipe.py && cd ~/buenos/ && python act_ultimos.py
