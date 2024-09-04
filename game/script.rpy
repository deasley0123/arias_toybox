# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aria", who_style="aria_say_label", what_style="aria_say_dialogue")
define a_excite = Character(
    "Aria", 
    who_style="aria_say_label",
    what_style="aria_say_dialogue", 
    what_textshader="jitter:3.0, 3.0"
)
define q = Character("???", who_style="aria_say_label", what_style="aria_say_dialogue")
define n = Character("")
define s = Character("Serena")
define j = Character("Jo")
define narrator = nvl_narrator
define centered_narrator = Character("", nvl=True, ypos=0.5)
transform shaking_center:
    ypos 0.5
    block:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
transform shaking:
    block:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat

# The game starts here.

label start:
    camera:
        perspective True

    # scene bg attic day

    # show aria smile wave:
    #     zoom 0.5
    #     xalign 0.5
    #     yalign 1.0

    # # These display lines of dialogue.

    # a "Hi there!!! My name is Aria!"

    # a "We dont have a script yet...{p}-so I hope you'll stay with me while you wait!" 

    jump scene0

label scene0:
    narrator "It was a rainy Tuesday night."
    narrator """
    You came home from work to your small studio apartment, changed into sweatpants, 
    grabbed a drink from the fridge and sat on the floor in front of your TV because
    it was more comfortable than your shitty IKEA couch.
    """
    narrator """
    You flipped through channels and eventually settled on a network game show you remembered 
    watching with your grandmother when you were little.
    """

    narrator "It's more commercials than content now, and you quickly got bored and started scrolling on your phone."

    nvl clear

    narrator "A friend of yours from high school posted some engagement photos. Another made a pregnancy announcement."

    narrator """
    You thought about congratulating them, but you haven't spoken to either of them in years.
    Best case scenario, they would invite you to some celebratory event you couldn't afford to attend. 
    """

    narrator """
    Besides, you've already called in enough days at work that requesting any more would probably get you fired.
    So instead you drank and kept scrolling, eyes half glazed over. 
    """

    narrator """
    Eventually you can't keep your eyes open at all anymore. You lean your head back against your couch
    and fall asleep, wishing you could be anyone and anywhere else.
    """
    
    nvl clear

    show text "When you open your eyes again, you are no longer in your apartment." at shaking_center
    n "{alpha=0.0}When you open your eyes again, you are no longer in your apartment" # This exists to set the autoplay speed right

    jump scene1


label scene1:
    scene bg attic day
    # show aria smile wave:
    #     zoom 0.5
    #     xalign 0.5
    #     yalign 1.0

    q "Hello? Helloooo? Is anyone in there?" with vpunch
    q "Blink twice if you can hear me! They're not blinking. THEY'RE NOT BLINKI-{p}Wait, you don't have eyelids."
    q "Uhhh... How about nodding? Maybe with a little help..."
    n "A small hand reaches out to touch your head. It's warm."
    q "Oh! You're moving. That's a great sign!"
    n "Above you is an unfamiliar ceiling. Pitched wooden beams over a small attic."
    n "Early light streams golden through the window. The morning birdsong is foreign but beautiful."
    n "The walls are strewn with drawings, the uneven floor littered with books and candles."
    n "There is a small, unmade bed in the corner, a disheveled arrangement of sheets and leather tomes."
    n "The owner of which (you assume) peers over her hat at you, uncomfortably close now."
    n "You shift away, and she skitters back."
    q "Hey! You moved! That's great!! It worked!! I'm AMAZING!!!"
    s "Where am I? Who are you? What's going on? Why-"
    n "You are becoming aware of your body in spurts. Currently seated, your hands support you."
    n "The ground feels tacky to touch, prompting you to really see it... and your hands."
    s "Why is the ground covered in blood? WHY ARE MY HANDS PAWS?!?"
    a "I'm Aria! You're my favorite doll!"
    a "{i}\"Jophiel the Duskborn, catfolk master thief\"{p}\"Right hand of the Weald Queen! Unmatched in the fields of battle AND wits-{/i}\""
    s "My name is Serena.{p}I'm an Uber driver from Cleveland."
    s "What on Earth are you talking about?"
    a "Ah! That's just the thing! You're not on Earth anymore at all!"
    a "I've summoned you here, {i}Jophiel{/i}, to help me perform a mighty deed.{p}We're going on A {b}{i}QUEST!{/i}{/b}"
    a_excite "AREN'T YOU EXCITED?!" with vpunch
    n "The young girl beams at you. The blood-drawn ritual circle under you is starting to dry on the raw wood planks."
    n "You make one last futile attempt at normalcy."
    s "Is this... is this some kind of TikTok trend? Is someone filming me right now?"
    a "What's a TikTok?{p}Is it like a clock?? I don't have a clock, silly!"
    a "I'm not allowed around time anymore."
    s "..."
    a "..."
    s "..."
    n "You change the subject."
    s "That hat... are you some kind of witch? Assuming any of this is real at all and it's not just a really weird dream."
    n "You had a slice of mushroom and black olive pizza last night, but they were just {i}button mushrooms{/i}, right? Not the other kind...?"
    a "Ahem. I am a SORCERESS, not a witch!\nThe hat is for style."
    n "She poses, obviously trying to appear cool.{p}You brush some dust off your knee and stand."
    n "You're a little taller than you were before, probably. There isn't anything familiar to measure against in here."
    s "Great, so you're a sorceress, and I'm a... toy? A five-foot talking cat?"
    n "You feel the pointed ears in your hair and the weight of a long, thin tail stretching out behind you."
    a "Well, Jophiel-"
    s "It's Serena."
    a "Hmmmm... That doesn't sound like much of a {i}quest{/i} name. \'Serenas\" don't really go to do great deeds."
    n "You almost interject about the accomplishments of the famous people on Earth who share your name."
    n "But it's not like you've ever really done anything, personally, so you bite your tongue."
    a "Besides! Didn't you want to be someone else?"
    n "Her question is genuine in a way children's questions often are, but your pulse quickens all the same."
    s "What do you mean?"
    s "...How did you know that?"
    a "Oh." 
    a "Well, it's a condition for my spell. I can only summon willing souls. It only works if you don't want to be who or where you are."
    a "I wouldn't want to pull you here if you were happier where you were."
    a "Soul magic like that makes me feel icky."
    n "This line of conversation is making you think about yourself more critically than is comfortable."
    n "You change the subject again."
    s "What about my body here, then? Shouldn't I be soft, small, and full of cotton stuffing or something?"
    a "Nope! I tried this spell before with lower quality stuff, but... it didn't work out."
    a "I HAD a rocking horse."
    a "Maple Stirrup, you will be remembered."
    a "I didn't really expect it to work with YOU either, but it's probably because Mom made Jophiel for me."
    a "She's a much more powerful Sorceress than me, so you must be made of quality stuff!"
    a "As soon as your soul took root, you became big like that!"
    s "Wow. Okay. So many questions about that. A lot to unpack there."
    n "You sense an opportunity. If her mother is a powerful sorceress as well, maybe she could fix whatever is going on here and send you home?"       
    s "So, uh, your mom is around then? I think we might be in need of some parental supervision."
    a "No, Mom is away conducting her research. She's been away for a while. It's just me here while she's gone."
    n "Aria's smile falls away for the first time since you woke. Her clear discomfort around this question gives you pause, but you push ahead regardless."
    s "Oh, well, if she's been away for a while then that must be our quest? Let's go and find your mom!"
    a "No, I'm forbidden from interfering with Mom's work."
    s "Oh. Then-"
    a "Our quest is something of far greater, far NOBLER importance!"
    s "Well, maybe-"
    a "Within this forest lies a creature foul and perverse.{p}To battle it is to court danger.{p}To challenge it is foolhardiness personified."        
    a "BUT IT MUST BE DONE! THE BOG BEAST MUST BE CAPTURED!"
    a_excite "AND IF IT IS NOT BY OUR HAND, THEN BY WHOSE!?"
    s "Anyone's! Yours! But not mine! I don't even have hands!?"
    a "But I'm not allowed in the forest without supervision.{p}And Mom is never around to supervise me."
    a "But you're an adult. You could supervise me..."
    n "This conversation is going nowhere. Or, at least, nowhere you want to go."
    s "Aria, please. I understand you're bored, and maybe a little lonely, but I can't stay here, okay?"
    s "I need to go home."
    a "..."
    a "I understand."
    s "Okay, good-"
    a "If that's what you really want, I will send you home."
    a "I promise."
    a "..."
    a "But I can only open a gate between worlds when the borders are thinnest."
    n "You feel a sinking weight in your stomach."
    s "When's that?"
    a "Dawn and Dusk."
    a "I can't send you home until tonight."
    n "The weight in your stomach grows."
    a "So, since I can't send you back yet anyways...{p}And I still need adult supervision..."
    n "You swallow hard and sigh. Her big eyes look up at you full of hope.{p}When was the last time you looked at anything like that?"
    s "Well, I've never been on any quests before. Certainly haven't encountered any bog beasts, so I don't know how much help I'll be."
    n "Even as you're speaking, you recognize that there isn't really a choice here."
    n "You can whine and drag your feet, but the little girl in front of you is powerful enough to summon you from another world, apparently."
    n "If she wants to go on a quest, you're going on a quest. You can't even get her to call you by your actual name."
    s "But first, before any questing, my name-"
    a "Jophiel."
    s "Serena."
    a "Jophiel."
    s "..."
    s "Jo."
    a "..."
    j "So, where is this bog beast anyhow?"
    a "The bog beast slumbers in the murk at the heart of this very forest."
    j "So...{p}Maybe 20 minutes?"
    a "More like an hour. I've got little legs."
    j "Better get moving then."
    n "With glee, she rushes to the window, throws it open, and lets down her sheets. You realize now that they've already been tied nicely for such a purpose."
    a "Down we go!"
    j "We're not gonna use the door?"
    a "Mom will know if we go that way! Besides, going out the window is how you always start an adventure!"
    n "She throws you one last smile before sliding over the sill and down out of sight."
    n "You sigh once more as you toss your own leg over and look down. The house is only one floor, plus this attic, so it isn't far to go."
    n "Aria waits impatiently on the ground below."
    a "What are you waiting for? Our quest awaits!"

    # This ends the game.

    return
