"""Build static editable karaoke markup from the song's aligned word timings."""
from pathlib import Path
import json
from html import escape
ROOT=Path(__file__).resolve().parent
source=json.loads((ROOT.parent/'data/allow-always-final.json').read_text())
cut=json.loads((ROOT/'assets/timing.json').read_text())['sourceStart']
duration=11.5192
specs=[(7,0,3.25,[2,1]),(8,3.25,7.15,[3,3]),(9,7.15,10.8,[3,2]),(10,10.8,duration,[2,1])]
markup=[];timings=[];manifest=[]
for group,(line,begin,end,lengths) in enumerate(specs):
    words=[w for w in source['words'] if w['line']==line]
    rows=[];cursor=0
    for count in lengths:
        row=[]
        for w in words[cursor:cursor+count]:
            key=f'karaoke-g{group}-w{cursor}'
            row.append(f'<span class="karaoke-word"><span>{escape(w["text"].upper())}</span><span id="{key}" class="karaoke-fill" aria-hidden="true">{escape(w["text"].upper())}</span></span>')
            a,b=w['start']-cut,w['end']-cut
            if a<duration and b>0:
                start=max(0,a);finish=min(duration,b)
                initial=100*(1-max(0,-a)/(b-a))
                final=100*(1-(finish-a)/(b-a))
                timings.append(f"tl.fromTo('#{key}',{{'--karaoke-progress':'{100-initial:.5f}%'}},{{'--karaoke-progress':'{100-final:.5f}%',duration:{finish-start:.6f},ease:'none',immediateRender:false}},{start:.6f});")
            manifest.append({'id':key,'text':w['text'],'start':a,'end':b})
            cursor+=1
        rows.append('<div class="karaoke-row">'+' '.join(row)+'</div>')
    markup.append(f'<section id="karaoke-line-{group}" class="clip karaoke-group" data-start="{begin}" data-duration="{end-begin:.6f}" data-track-index="0"><div class="karaoke-lyric">'+''.join(rows)+'</div></section>')
html='''<!doctype html><html><body><template>
<!-- Per-word clip-path wipe adapted from the HyperFrames caption-clip-wipe component. -->
<style>
@font-face {font-family:'Retro Karaoke';src:url('assets/fonts/Arial-Bold-Italic.ttf') format('truetype');font-style:italic;font-weight:700;font-display:block}
#root {position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.karaoke-group {position:absolute;inset:0;pointer-events:none}
.karaoke-lyric {position:absolute;left:90px;right:115px;top:235px;text-align:center;font-family:'Retro Karaoke';font-size:82px;font-weight:700;font-style:italic;line-height:1.16;letter-spacing:0.005em;color:#fff2c4}
.karaoke-row {display:block;white-space:nowrap}
.karaoke-word {position:relative;display:inline-block;padding:0 5px;-webkit-text-stroke:5px #21162e;paint-order:stroke fill;text-shadow:5px 5px 0 #41b5c2,8px 8px 0 #21162e}
.karaoke-fill {position:absolute;inset:0;color:#ff70ac;--karaoke-progress:0%;clip-path:inset(0 calc(100% - var(--karaoke-progress)) 0 0);text-shadow:none}
</style>
<div id="root" data-composition-id="karaoke" data-width="1080" data-height="1920" data-duration="11.5192">
'''+ '\n'.join(markup)+'''
</div>
<script>
const tl=gsap.timeline({paused:true});
'''+ '\n'.join(timings)+'''
window.__timelines=window.__timelines||{};
window.__timelines['karaoke']=tl;
</script>
</template></body></html>
'''
(ROOT/'compositions/karaoke.html').write_text(html)
(ROOT/'assets/karaoke-words.json').write_text(json.dumps({'source':'../data/allow-always-final.json','sourceStart':cut,'words':manifest},indent=2)+'\n')
