################################################################################
#  CHARACTER DEFINITIONS
################################################################################
define jus = Character("Justine", color="#335a3b", who_style="namebox")
define g   = Character("Guard",   color="#207476", who_style="sec_namebox")
define k = Character("Kim",     color="#e84393", who_style="sec_namebox")
define c   = Character("Carl",    color="#113d29", who_style="sec_namebox")
define n = Character("Nurse", color="#E9967A", who_style="sec_namebox")
define ma = Character("Mae", color="#E23A32", who_style="sec_namebox")
define m = Character("Mae", color="#E23A32", who_style="namebox")
define s = Character("Sophie", color="#A23A32", who_style="sec_namebox")
define l = Character("Lyn", color="#AB3A32", who_style="sec_namebox")
define e = Character("Ella", color= "#3A3AB4", who_style="sec_namebox")
define v = Character("Vidal", color="#3A3AB4", who_style="sec_namebox")
define cs = Character("Cashier", color="#09091e", who_style="sec_namebox")
define j = Character("Joriemer", color="#519c90", who_style="sec_namebox")

define gui.name_text_size = 100  # Change 40 to your desired font size

################################################################################
#  TRANSFORMS
################################################################################
transform justine_bottom_left:
    xalign 0.0        # left edge
    yalign 1.0        # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.8          # tweak if she’s still too big

transform kim_bottom_right:
    xalign 0.75       # left edge
    yalign 1.05       # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.8          # tweak if she’s still too big

transform justine_bottom_center:
    xalign 0.3     # left edge
    yalign 0.9       # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.7          # tweak if she’s still too big

transform kim_bottom_center:
    xalign 0.5
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform kim_bottom_left:
    xalign 0.2
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform guard_bottom_right:
    xalign 0.75       # left edge
    yalign 1.1        # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.8          # tweak if she’s still too big

transform mae_bottom_center:
    xalign 0.3     # left edge
    yalign 0.9       # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.7          # tweak if she’s still too big

transform sophie_bottom_center:
    xalign 0.5
    yalign 0.9
    anchor (0.0, 1.0)

transform mae_bottom_left:
    xalign 0.0        # left edge
    yalign 1.0        # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.7          # tweak if she’s still too big

################################################################################
#  IMAGE_DEFINITIONS+-
################################################################################

#_backgrounds__ (make sure these files exist in /game/images/)
image bg_gate              = "images/bg_gate.jpg"
image bg_after_school_gate = "images/after_school_gate.jpg"
image bg_pub_lib_door      = "images/pub_lib_door.jpg"
image bg_guard_house       = "images/guard_house.jpg"
image bg_room              = "images/bg_room.jpg"
image splash_bg            = "images/splash_bg.png"
image bg_far_view_entrance      = "images/FarViewofEntranceArea.jpg"
image bg_new_building1     = "images/new_building1.jpg" 
image bg_new_building2     = "images/new_building2.jpg"
image bg_new_building3     = "images/new_building3.jpg"
image bg_new_building4     = "images/new_building4.jpg"  
image bg_new_building5     = "images/new_building5.jpg"
image bg_new_building6     = "images/new_building6.jpg"
image bg_nearing_new_building   = "images/NearingNewBuilding.jpg"
image bg_tambayan_to_entrance   = "images/TambayanAreaGoingtoEntrance.jpg"
image bg_circle_area_lower_view = "images/CircleAreaLowerView.jpg"
image bg_vendor            = "images/vendor.jpg"
image bg_vendor_view       = "images/vendor_view.jpg"
image Enter_choice2 = "images/Enter_choice2.jpg"
image bg_entering_hideout      = "images/Entering_hideout.jpg"
image bg_closed_hideout_gate   = "images/Closed_hideout_area_gate.jpg"
image bg_entering_the_school_lobby = "images/entering_the_school_lobby.jpg"
image bg_pup_lobby = "images/pup_lobby.jpg"
image bg_informationdesk = "images/informationdesk.jpg"
image bg_window1 = "images/window1.jpg"
image floor1_hallwayright = "images/floor1_hallwayright.jpg"
image bg_acad = "images/acad.jpg"
image bg_sas = "images/sas.jpg"
image bg_midstair = "images/mid_boys_stairs.jpg"
image bg_lgbt1 = "images/lgbt_cr.jpg"
image bg_lgbt2 = "images/lgbt_door.jpg"
image bg_lgbt3 = "images/lgbt_halfway.jpg"
image bg_stair1 = "images/first_stair1.jpg"  
image bg_stair2= "images/first_stair2.jpg"
image bg_stair3= "images/first_stair3.jpg"
image bg_stair4= "images/first_stair4.jpg"
image bg_stair5 = "images/first_stair5.jpg"
image bg_stair6 = "images/first_stair6.jpg"
image fire_exit1 = "images/fire_exit1.jpg"
image fire_exit2 = "images/fire_exit2.jpg"
image m1 = "images/m1.jpg"
image m2 = "images/m2.jpg"
image m3 = "images/m3.jpg"
image m4 = "images/m4.jpg"
image m5 = "images/m5.jpg"
image sf1 = "images/sf1.jpg"
image sf2 = "images/sf2.jpg"
image sf3 = "images/sf3.jpg"
image sf4 = "images/sf4.jpg"
image sf5 = "images/sf5.jpg"
image sf6 = "images/sf6.jpg"
image sf7 = "images/sf7.jpg"
image sf8 = "images/sf8.jpg"
image sf9 = "images/sf9.jpg"
image sf10 = "images/sf10.jpg"
image sf11 = "images/sf11.jpg"
image sf12 = "images/sf12.jpg"
image sf13 = "images/sf13.jpg"
image sf14 = "images/sf14.jpg"
image sf15 = "images/sf15.jpg"
image sf16 = "images/sf16.png"
image sf17 = "images/sf17.jpg"
image floor1_midhallwayleft = "images/floor1_midhallwayleft.jpg"
image floor1_hallwayleft = "images/floor1_hallwayleft.jpg"
image left_halfway_ground1 = "images/left_halfway_ground1.jpg"
image left_halfway_ground2 = "images/left_halfway_ground2.jpg"
image left_halfway_ground3 = "images/left_halfway_ground3.jpg"
image left_halfway_ground4 = "images/left_halfway_ground4.jpg"
image left_halfway_ground5 = "images/left_halfway_ground5.jpg"
image faculty_inside = "images/faculty_inside.jpg"
image pet_cat = "images/petcat.jpg"
image science_lab = "images/science_lab.jpg"
image rightside_staircase = "images/rightside_staircase.jpg"
image chair = "images/chair.jpg"
image chair1 = "images/chair1.jpg"
image lobbychairs = "images/lobbychairs.jpg"

image g1 = "images/g1.jpg"
image g2 = "images/g2.jpg"
image g3 = "images/g3.jpg"
image g4 = "images/g4.jpg"
image g5 = "images/g5.jpg"
image g6 = "images/g6.jpg"
image g7 = "images/g7.jpg"
image g8 = "images/g8.jpg"
image g9 = "images/g9.jpg"
image g10 = "images/g10.jpg"
image g11 = "images/g11.jpg"
image g12 = "images/g12.jpg"

image hideout_fireexit = "images/hideout_fireexit.jpg"
image hideout_extension = "images/hideout_extension.jpg"

# __GARDEN__ and __EXIT__ (make sure these files exist in /game/imgaes/)
image bg_garden = "images/garden.jpg"
image bg_garden_cat = "images/view_cat.jpg"
image bg_garden1 = "images/garden1.jpg"
image bg_garden2 = "images/garden2.jpg"
image bg_garden3 = "images/garden3.jpg"
image bg_back_garden1 = "images/back_garden1.jpg"
image bg_exit1 = "images/exit1.jpg"
image bg_exit2 = "images/exit2.jpg"
image bg_exit3 = "images/exit3.jpg"
image bg_exit4 = "images/exit4.jpg"
image bg_exit5 = "images/exit5.jpg"
image bg_exit6 = "images/exit6.jpg"
image bg_exit7 = "images/exit7.jpg"
image bg_exit8 = "images/exit8.jpg"
image bg_exit9 = "images/exit9.jpg"
image bg_exit10 = "images/exit10.jpg"
image bg_fire_exit_inside1 = "images/fire_exit_inside1.jpg"
image bg_fire_exit_inside2 = "images/fire_exit_inside2.jpg"
image bg_fire_exit_inside3 = "images/fire_exit_inside3.jpg"
image bg_fire_exit_inside4 = "images/fire_exit_inside4.jpg"
image bg_fire_exit_inside5 = "images/fire_exit_inside5.jpg"
image library1 = "images/library1.jpg"
image library2 = "images/library2.jpg"
image discussion = "images/discussion.jpg"


# _Floor 2__ (make sure these files exist in /game/images/)
image bg_floor2_halfwayright = "images/floor2_halfwayright.jpg"

#___DOCUMENTS__ PROCESS___
image doc1 = "images/doc1.jpg"
image doc2 = "images/doc2.jpg"
image doc3 = "images/doc3.jpg"
image doc4 = "images/doc4.jpg"


image bg_admin_office = "images/admin_office.jpg"
image bg_authorized_exit = "images/authorized_personnelonlyareaexit.jpg"
image bg_avr = "images/avr.jpg"
image bg_avr_door = "images/avrdoor.jpg"
image bg_beside_avr = "images/besideavr.jpg"
image bg_beside_faculty_office = "images/besidefacultyoffice.jpg"
image bg_cashier_window = "images/cashierwindow.jpg"
image clinic1 = "images/clinic_inside.jpg"
image clinic2 = "images/clinic_outside.jpg"


# Up to the 3rd Floor
image stair1 = "images/stair1.jpg"
image stair2 = "images/stair2.jpg"
image stair3 = "images/stair3.jpg"
image stair4 = "images/stair4.jpg"
image stair5 = "images/stair5.jpg"

# Third floor left to the right
image hallway1 = "images/hallway1.jpg"
image hallway2 = "images/hallway2.jpg"
image hallway3 = "images/hallway3.jpg"
image hallway4 = "images/hallway4.jpg"
image hallway5 = "images/hallway5.jpg"
image hallway6 = "images/hallway6.jpg"
image hallway7 = "images/hallway7.jpg"
image hallway8 = "images/hallway8.jpg"
image hallway9 = "images/hallway9.jpg"

# Room 305 Scene
image room307_1 = "images/room307_1.jpg"
image room307_1 = "images/room307_1.jpg"
image room307_1 = "images/room307_1.jpg"
image room307_1 = "images/room307_1.jpg" 

# Room 307 Scene
image room307_1 = "images/room307_1.jpg"
image room307_2 = "images/room307_2.jpg"
image room307_3 = "images/room307_3.jpg"

# Girl's CR
image girls1 = "images/girls1.jpg"
image girls2 = "images/girls2.jpg"
image girls3 = "images/girls3.jpg"
image girls4 = "images/girls4.jpg"

# Rooms
image room1 = "images/room1.jpg"
image room2 = "images/room2.jpg"

# Fourth Floor
image 1 = "images/1.jpg"
image 2 = "images/2.jpg"
image 3 = "images/3.jpg"

# 4th Hallway
image f1 = "images/f1.jpg"
image f2 = "images/f2.jpg"
image f3 = "images/f3.jpg"
image f4 = "images/f4.jpg"
image f5 = "images/f5.jpg"
image f6 = "images/f6.jpg"
image f7 = "images/f7.jpg"
image f8 = "images/f8.jpg"
image f9 = "images/f9.jpg"
image f10 = "images/f10.jpg"
image f11 = "images/f11.jpg"

# Fourth Room
image comlab = "images/comlab.jpg"
image comhardware = "images/comhardware.jpg"
image housekeeping_room = "images/housekeeping_room.jpg"
image travel_and_tours_room1 = "images/travel_and_tours_room1.jpg"
image travel_and_tours_room2 = "images/travel_and_tours_room2.jpg"
image student_org1 = "images/student_org1.jpg"
image hm_storage_room1 = "images/hm_storage_room1.jpg"
image kitchen_lab2 = "images/kitchen_lab2.jpg"
image proj = "images/proj.jpg"
image food_and_bev_room2 = "images/food_and_bev_room2.jpg"
image csc_room1 = "images/csc_room1.jpg"
image csc_room2 = "images/csc_room2.jpg"
image lab_management = "images/lab_management.jpg"
image standard_room = "images/standard_room.jpg"
image deluxe = "images/deluxe.jpg"

# Roof Deck
image rf1 = "images/rf1.jpg"
image rf2 = "images/rf2.jpg"
image rf3 = "images/rf3.jpg"
image rf4 = "images/rf4.jpg"
image rf5 = "images/rf5.jpg"


image nurse_normal = im.Scale("images/nurse_normal.png", 925, 1200)


#_Cashier_
image Cashier_talking = im.Scale("images/cashier_talking.png", 1200, 1350)
image Cashier_normal = im.Scale("images/cashier_normal.png", 925, 1200)


#_Carl_
image Carl_normal      = im.Scale("images/Carl_normal.png", 1200, 1350)
image Carl_talking     = im.Scale("images/Carl_talking.png", 1200, 1300)
image Carl_suggesting  = im.Scale("images/Carl_suggesting.png", 1200, 1300)
image Carl_thinking    = im.Scale("images/Carl_thinking.png", 1200, 1300)

#_Justine_ (925×1200, all tags use a single underscore)
image Justine_normal         = im.Scale("images/Justine_normal.png",        925, 1200)
image Justine_talking        = im.Scale("images/Justine_talking.png",       925, 1200)
image Justine_happy          = im.Scale("images/Justine_happy.png",         925, 1200)
image Justine_alarmed        = im.Scale("images/Justine_alarmed.png",       925, 1200)
image Justine_disappointed     = im.Scale("images/Justine_disappointed.png",      925, 1200)
image Justine_crying         = im.Scale("images/Justine_crying.png",        925, 1200)
image Justine_holding_id     = im.Scale("images/Justine_holding_id.png",    925, 1200)
image Justine_holding_phone  = im.Scale("images/Justine_holding_phone.png", 925, 1200) 
image Justine_waving        = im.Scale("images/Justine_waving.png",       925, 1200)
image Justine_Sighing           = im.Scale("images/Justine_Sighing.png",          925, 1200)
image Justine_smiling          = im.Scale("images/Justine_smiling.png",         925, 1200)
image Justine_realised      = im.Scale("images/Justine_realised.png",     925, 1200)
image Justine_sad          = im.Scale("images/Justine_sad_smile.png",         925, 1200)
image Justine_laughing     = im.Scale("images/Justine_laughing.png",         925, 1200)
image Justine_scared    = im.Scale("images/Justine_scared.png",         925, 1200)

#__KIM__
# Assuming Kim's images are in /game/images/ and you want a similar size to Carl (1200x1300)
image Kim_normal       = im.Scale("images/kim_normal.png",       925, 1200)
image Kim_holdingID    = im.Scale("images/kim_holdingID.png",    925, 1200)
image Kim_smiling      = im.Scale("images/kim_smiling.png",      925, 1200)
image Kim_talking      = im.Scale("images/kim_talking.png",      925, 1200)
image Kim_calling      = im.Scale("images/kim_calling.png",      925, 1200)

#_Guard_
image Guard normal   = im.Scale("images/guard_normal.png",          925, 1200)
image Guard happy    = im.Scale("images/guard_happy_talking.png",   925, 1200)
image Guard annoyed  = im.Scale("images/guard_talking_annoyed.png", 925, 1200)
image Guard angry    = im.Scale("images/guard_talking_angry.png", 925, 1200)



#_LYN_
image Lyn_talking           = im.Scale("images/Lyn_talking.png",        925, 1200)
image Lyn_angry             = im.Scale("images/Lyn_angry.png",        925, 1200)
image Lyn_Anya_smirk        = im.Scale("images/Lyn_Anya_smirk.png",        925, 1200)
image Lyn_disgusted         = im.Scale("images/Lyn_disgusted.png",        925, 1200)
image Lyn_normal            = im.Scale("images/Lyn_normal.png",        925, 1200)
image Lyn_pouting_talking   = im.Scale("images/Lyn_pouting_talking.png",        925, 1200)
image Lyn_pouting           = im.Scale("images/Lyn_pouting.png",        925, 1200)
image Lyn_smug              = im.Scale("images/Lyn_smug.png",        925, 1200)
image Lyn_talking           = im.Scale("images/Lyn_talking.png",        925, 1200)
image Lyn_worried           = im.Scale("images/Lyn_worried.png",        925, 1200)


#_ELLA_
image Ella_grinning         = im.Scale("images/Ella_grinning.png",        925, 1200)
image Ella_normal           = im.Scale("images/Ella_normal.png",        925, 1200)
image Ella_smiling          = im.Scale("images/Ella_smiling.png",        925, 1200)
image Ella_talking          = im.Scale("images/Ella_talking.png",        925, 1200)
image Ella_whispering       = im.Scale("images/Ella_whispering.png",        925, 1200)

#_VIDAL_
image Vidal_angry_talking   = im.Scale("images/Vidal_angry_talking.png",    925, 1200)
image Vidal_angry           = im.Scale("images/Vidal_angry.png",        925, 1200)
image Vidal_normal          = im.Scale("images/Vidal_normal.png",        925, 1200)
image Vidal_smiling         = im.Scale("images/Vidal_smiling.png",        925, 1200)
image Vidal_talking         = im.Scale("images/Vidal_talking.png",        925, 1200)

#_SOPHIE_
image Sophie_normal         = im.Scale("images/Sophie_normal.png",        925, 1200)
image Sophie_smiling        = im.Scale("images/Sophie_smiling.png",        925, 1200)
image Sophie_talking        = im.Scale("images/Sophie_talking.png",        925, 1200)

#_JORIE_
image Jorie_normal          = im.Scale("images/Jorie_normal.png",        925, 1200)
image Jorie_smiling         = im.Scale("images/Jorie_smiling.png",        925, 1200)
image Jorie_talking         = im.Scale("images/Jorie_talking.png",        925, 1200)

#_MAE_
image Mae_holding_paper     = im.Scale("images/Mae_holding_paper.png",        925, 1200)
image Mae_normal            = im.Scale("images/Mae_normal.png",        925, 1200)
image Mae_smiling           = im.Scale("images/Mae_smiling.png",        925, 1200)
image Mae_talking           = im.Scale("images/Mae_talking.png",        925, 1200)

# Jorieee
image Jorie_normal            = im.Scale("images/Jorie_normal.png",        925, 1200)
image Jorie_smiling           = im.Scale("images/Jorie_smiling.png",        925, 1200)
image Jorie_talking           = im.Scale("images/Jorie_talking.png",  925, 1200)

# Faculty
image Faculty_normal           = im.Scale("images/Faculty_normal.png",        925, 1200)
image Faculty_talking           = im.Scale("images/Faculty_talking.png",  925, 1200)

transform justine_bottom_left:
    xalign 0.0
    yalign 1.0
    zoom 0.6

default visited_library = False
default visited_stone_circle = False
default visited_vendor = False
default visited_hideout = False

default visited_cashier      = False
default visited_faculty      = False
default visited_avr          = False
default visited_admin        = False
default visited_sas          = False
default visited_clinic       = False
default visited_fire_exit    = False
default visited_pup_library  = False
default visited_room_204     = False
default visited_room_302     = False
default visited_girls_cr     = False
default visited_comlab       = False
default visited_project_proposal = False
default visited_lab_management = False
default visited_food_beverage = False
default visited_org          = False
default visited_housekeeping_room = False
default visited_csc          = False
default visited_deluxe_room  = False
default visited_standard_room = False
default visited_travel_tours = False


label before_main_menu:
    $ apply_ui_theme()
    return

$ persistent.ui_theme = "dark"

default persistent.ui_theme = "default"  # This saves the user's selected theme

init python:

    def apply_ui_theme():
        # Use persistent color or default to white
        text_color = persistent.text_color if hasattr(persistent, "text_color") else "#5fa121"

        # Change the say dialogue text color
        style.say_dialogue.color = text_color

        # Optionally, change window background text color or other UI elements here too
        # For example, change textbox window text color or font color if needed

        # To refresh styles immediately, call:
        renpy.restart_interaction()


label start:
    stop music fadeout 1.0
    scene bg_room at Transform(xysize=(3280, 3220))

    show Carl_normal at center with dissolve
    c "Hey there."

    show Carl_talking at center with dissolve
    c "Are you new to visual novels?"

    menu:
        "I'm new at this, sorry.":
            jump tutorial
        "I already know, thank you.":
            jump skip_tutorial

label tutorial:

    show Carl_suggesting at center with dissolve
    c "No worries! I'm here to guide you around."

    show Carl_talking at center with dissolve
    c "This box below me? That's the text box."

    show Carl_thinking at center with dissolve
    c "All the story, dialogue, and narration happens here."

    show Carl_suggesting at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    show Carl_suggesting at center with dissolve
    c "You can also roll back to dialogue with ease using your scroll wheel in you mouse!"

    show Carl_thinking at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    show Carl_talking at center with dissolve
    c "You can press H again to bring everything back."

    show Carl_thinking at center with dissolve
    c "Now if you press the Esc key, you'll open the game menu."

    show Carl_normal at center with dissolve
    c "Let me explain the buttons there real quick!"

    show Carl_talking at center with dissolve
    c "History – lets you view past dialogue in case you missed something."

    show Carl_suggesting at center with dissolve
    c "Save and Load – save your progress or return to a previous point."

    show Carl_thinking at center with dissolve
    c "Preferences – change text speed, music volume, and other settings."

    show Carl_talking at center with dissolve
    c "About – gives info about the game."

    show Carl_normal at center with dissolve
    c "Help – shows all the controls."

    show Carl_thinking at center with dissolve
    c "And Quit – well... exits the game. Careful with that one."

    show Carl_suggesting at center with dissolve
    c "And don't forget the Return button – it brings you right back to the game."

    show Carl_talking at center with dissolve
    c "Got it? Sweet. Let's get started!"

    jump main_game

label skip_tutorial:

    show Carl_normal at center with dissolve
    c "Ah, a veteran I see. I'll leave you to it then."

    jump main_game

label main_game:

    show Carl_talking at center with dissolve
    c "This is where the real story begins..."

    # Continue your actual visual novel story from here...

    scene bg_gate at Transform(xysize=(2580, 1520)) with fade

    show Justine_normal at justine_bottom_left
    jus "Wow, hindi ako makapaniwala na malapit na akong umalis sa sintang paaralang ‘to."

    # The guard appears
    show Guard normal at guard_bottom_right with dissolve
    g "Good morning, iho. Asan yung I.D mo?"
    
    show Justine_talking at justine_bottom_left
    jus "Sorry po kuya, naiwan ko po yung I.D ko."

    show Guard annoyed at guard_bottom_right with dissolve
    g "Ayy, pasensya na iho pero bawal kang pumasok pag wala kang I.D."

    # CHOICE MENU -------------------------------------------------------------
    menu:
        "Bumalik na lang ako sa bahay":
            jump go_home
        "Tawagan si Kim para kuhanin ang I.D":
            jump call_kim

################################################################################
# CHOICE 1 – GO HOME –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label go_home:

    show Justine_talking at justine_bottom_left
    jus "Ayy ganon po ba… sige po kuya, uwi na lang po ako."

    show Guard normal
    g "Sa susunod, siguraduhing may I.D ka ha."

    hide Guard normal at guard_bottom_right with dissolve
    show Justine_talking
    $ renpy.pause(0.3)

    # short inner monologue
    window hide
    show Justine_normal at justine_bottom_left
    hide Justine_normal
    with None
    $ renpy.pause(0.2)
    window show

    jus "(Grabe nakalimutan ko nga pala ang higpit pala ng guard pero ok lang atleast safe ang estudyante dito sa higpit ng guard,)"
    jus "(kaysa naman sa ibang school may guard nga pero wala namang pakialam pano nalang kung may insidente, at least dito samin safe naman.)"
    jus "(hayss, nu bayan pagbabalik pa ko malalate din naman ako, hindi pa nagpapapasok yung prof namin kapag late, sige na nga bukas nalang ako papasok.)"

    "THE END"
    return

################################################################################
# CHOICE 2 – CALL KIM ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label call_kim:

    show Justine_talking at justine_bottom_left
    jus "Ayy ganon po ba, wait lang kuya. Papakuha ko lang I.D ko."
    hide Justine_talking
    # phone sprite
    show Justine_holding_phone at justine_bottom_left
    "Tumawag si Justine sa kanyang kaibigan…"
    hide Justine_holding_phone
    jus "Hi Kim, nasaan ka ngayon?"
    k "Nasa bahay pa. Bakit?"
    jus "Pwede ka bang dumaan sa bahay ko at kunin ang I.D ko? Naiwan ko eh."
    k "Sakto, may aasikasuhin din ako sa school. Pupuntahan kita."

    "Ilang minuto ang lumipas…"
    hide Guard normal with dissolve
    show Kim_holdingID at kim_bottom_right with dissolve
    k "Jas! Eto na I.D mo!"
    hide Kim_holdingID with dissolve

    show Justine_holding_id at justine_bottom_left
    show Kim_normal at kim_bottom_left with dissolve
    jus "Ayos! Salamat!"
    hide Kim_normal with dissolve
    hide Justine_holding_id

    

    # show guard happy and let them pass
    show Guard happy at guard_bottom_right with dissolve
    g "Hmm… sige, pwede na kayong pumasok."

    hide Guard happy with dissolve
    hide Justine_holding_phone
    hide Justine_talking
    hide Justine_normal
    show Kim_smiling at kim_bottom_center 
    show Justine_smiling at justine_bottom_center 
    jus "Salamat po, kuya Guard!"
    hide Guard talking
    hide Kim_normal
    

    hide Kim_holdingID with dissolve
    scene bg_guard_house at Transform(xysize=(2580, 1520)) with fade


label hub_room:

    scene bg_after_school_gate at Transform(xysize=(2580, 1720)) with fade 
    show Justine_normal at justine_bottom_left

    jus "Mhmmmm?"

    call screen nav_door_gate
    return

label door_label:

    if visited_library:
        show Justine_Sighing at justine_bottom_left
        jus "Sarado na ang public library. Kanina pa tayo dumaan doon."
        jump hub_room
    else:
        $ visited_library = True

        show Justine_happy at justine_bottom_left
        jus "Ohhh, yung Public Library... ang dami naming alaala dito.…"

        scene bg_pub_lib_door at Transform(xysize=(2580, 1720)) with fade 
        show Justine_smiling at justine_bottom_left
        jus "Dito kami lagi natambay ng mga kaibigan ko sa tuwing may vacant kami."

        show Justine_talking at justine_bottom_left
        jus "Minsan sabay-sabay kaming gumagawa ng homework dito, pero mas madalas puro kwentuhan lang talaga."

        show Justine_laughing at justine_bottom_left
        jus "May isang beses pa nga, napagalitan kami ng librarian kasi masyado kaming maingay!"

        show Justine_Sighing at justine_bottom_left
        jus "Kung tama ang pagka-alala ko... open to every weekdays, 8 AM to 5 PM."
        hide Justine_Sighing

        show Justine_smiling at justine_bottom_left
        jus "Kaya minsan napapaovertime yung mga staff dito kasi di namin namamalayan — 5 na pala."

        show Justine_smiling at justine_bottom_left
        jus "Hay... nami-miss ko ‘yung mga ganung araw. Para bang ang gaan ng lahat."

        jump hub_room

label explore_new_building:

    if not persistent.visited_explore_new_building:
        $ persistent.visited_explore_new_building = True

        # First time dialogue
        scene bg_nearing_new_building at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_Sighing at justine_bottom_left
        jus "Grabe... matatapos na 'yung school year, pero 'tong building na 'to, hindi pa rin tapos."

        show Justine_Sighing at justine_bottom_left
        jus "Parang hindi rin ako makaka-graduate kung hihintayin ko 'yang matapos."
        jus "I wonder, magkakaroon kaya ng bagong program dito?"

        show Justine_normal at justine_bottom_left
        jus "Hay... sana naman, pagbalik ko next sem, may progreso na."

    else:
        # Alternate one-liner on revisits
        scene bg_nearing_new_building at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        scene bg_new_building1 at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        scene bg_new_building2 at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        scene bg_new_building3 at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        scene bg_new_building4 at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        scene bg_new_building5 at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        scene bg_new_building6 at Transform(xysize=(2580, 1520)) with fade
        pause 0.1
        show Justine_talking at justine_bottom_left with dissolve
        jus "Gina-gawa parin hanggang ngayon."
        hide Justine_talking
        scene bg_new_building6 at Transform(xysize=(2580, 1520))  

        pause

    # Return to choice menu after
    jump callscreen


label callscreen:
    scene bg_far_view_entrance at Transform(xysize=(2580, 1520)) with fade 
    call screen custom_choice_menu
    return



label resting_ground:
    scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with dissolve
    show Justine_happy at justine_bottom_left
    jus "Ang tahimik dito ngayon ha."
    hide Justine_happy

    jump choicethree

label choicethree:
    scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with fade
    call screen rest_choice_menu
    return

label stone_circle:

    if not visited_stone_circle:
        $ visited_stone_circle = True

        scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_happy at justine_bottom_left
        jus "Ahh, eto lagi pagkatapos ng klase."
        jus "Grabe kami makatakbo kasi inuunahan namin 'yung ibang estudyante—"

        scene bg_circle_area_lower_view at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_laughing at justine_bottom_left
        jus "…baka mawalan kami ng pwesto, kasi dito kami kumakain tuwing lunch time."

    else:
        scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_happy at justine_bottom_left
        jus "Ka-miss magkipag chismis dito haha"
        hide Justine_happy

    jump choicethree

label vendor:
    
    scene bg_vendor_view at Transform(xysize=(2580, 1520)) with fade
    show vendor_talking at right
    "Oyyyy, pogi bili kana"

    menu:
        "Bumili":
            jump bumili
        "Huwag bumili":
            jump huwag_bumili

label bumili:
    scene bg_vendor at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left 
    jus "Kuya, magkano po yung softdrinks?"
    hide Justine_talking

    show vendor_talking at right
    "Anong softdrinks?"
    hide vendor_talking

    show Justine_talking at justine_bottom_left
    jus "Coke po"
    hide Justine_talking

    show vendor_talking at right
    "Sige, ito oh"

    show Justine_talking at justine_bottom_left 
    jus "Salamat po"
    hide Justine_talking
    jump choicethree

label huwag_bumili:
    scene bg_vendor_view at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left
    jus "Salamat na lang po"
    hide Justine_talking

    show vendor_talking at right
    "Sure ka pogi? Baka gutom ka na?"
    hide vendor_talking

    show Justine_talking at justine_bottom_left 
    jus "haha... next time na lang po"
    hide Justine_talking

    jump choicethree
label hideout:
    scene bg_vendor_view at Transform(xysize=(2580, 1520)) with fade

    show Justine_laughing at justine_bottom_left
    jus "Solid netong tambayan na to! Sa dulo kaso sarado"

    menu:
        "Greet the Guard":
            jump greet_guard
        "Just walk away":
            jump walk_away
    pause

label greet_guard:
    scene bg_entering_hideout at Transform(xysize=(2580, 1520)) with dissolve
    show Justine_happy at justine_bottom_left 
    jus "Hmmm? Oh eto yung hideout according sa the boys"
    jus "Pero siguro ang pinaka-memorable kong time sa lugar na ito..."
    jus "is siguro yung nag open forum kami...."

    show Justine_Sighing at justine_bottom_left 
    jus "Hays, hindi ko parin makalimutan yung memory yun, grabe ang awkward ng atmosphere"
    hide Justine_Sighing with dissolve

    jump choicethree

label walk_away:
    scene bg_entering_hideout at Transform(xysize=(2580, 1520)) with fade
    show Guard annoyed at guard_bottom_right with dissolve
    g "oyy, oyy ano ginagawa mo dito?"
    hide Guard annoyed with dissolve

    show Justine_talking at justine_bottom_left
    jus "ahh, nag-iikot ikot lang po"
    hide Justine_talking with dissolve

    show Guard angry at guard_bottom_right
    g "di mo ba alam na bawal pumasok dito ng walang paalam?!"
    hide Guard angry with dissolve

    show Justine_scared at justine_bottom_left
    jus "sorry po kuya guard aalis na po ako…"
    hide Justine_scared with dissolve

    show Guard annoyed at guard_bottom_right with dissolve
    g "wag na mauulit to kung hindi i-re-report kita sa SAS"
    hide Guard annoyed with dissolve

    jump choicethree

################################################################################
#  ENTER BUILDING – Lobby hub
################################################################################
label enter_buildingcampus:

    scene bg_entering_the_school_lobby at Transform(xysize=(2580,1520)) with fade
    show Justine_normal at justine_bottom_left
    jus "Pasok tayo sa main building. Saan kaya pupunta ngayon?"
    scene bg_informationdesk at Transform(xysize=(2580,1520)) with fade
    show Justine_normal at justine_bottom_left
    scene bg_pup_lobby at Transform(xysize=(2580,1520)) with fade 
    
    jump inside_building

label inside_building:
    scene bg_window1 at Transform(xysize=(2580,1520)) with fade 
    call screen inside_choice_menu
    call screen information_desk
    return

label cashier:

    scene bg_cashier_window at Transform(xysize=(2580, 1520)) with fade
    show Justine_smiling at justine_bottom_left
    
    jus "Cashier… mabuti na wala ako kailangan na bayarin"

    jus "Tinamad pa kasi sa ibang subjects and yan tuloy bumayad pa siya ng tuition para sa tatlong semesters…"

    show Cashier_talking at kim_bottom_right
    cs "Hello, may babayaran pa ba kayo ngayon?"
    hide Cashier_talking

    show Justine_smiling at justine_bottom_left
    jus "Ay wala naman na po, pasensya na sa pagabala."

    show Cashier_talking at kim_bottom_right
    cs "Okay lang po. Kung may transaction kayo na gagawin,"
    cs "Pwede po kayo magbayad online sa PUP SIS..."
    cs "...o dalhin mo nalang ID mo dito para ma-verify ang transaction niyo po."
    hide Cashier_talking

    jump left_ground_1

label right_hall:
    scene floor1_hallwayright at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "grabe walang katao tao himala?"
    hide Justine_Sighing

label floor1_right_hall:
    scene floor1_hallwayright at Transform(xysize=(2580, 1520))  
    call screen right_hall_menu
    return
label clinic_room:

    scene clinic2 at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left

    jus "Clinic… ayan, tahimik pero dito sikat ang lahat ng drama sa buhay."

    show Justine_normal at justine_bottom_left
    jus "Dito ako tumatambay minsan dahil sa sakit ng ulo, pati na din dahil sa minsan na pasakit ng loob."

    show Justine_Sighing at justine_bottom_left
    jus "Minsang umupo ako d’yan"
    jus "hindi dahil sa masamang pakiramdam kundi dahil gusto ko lang ng pahinga."
    jus "At ang Nurse? Parang naging nanay ko pa."

    show Justine_smiling at justine_bottom_left
    jus "Palagi niya akong tinatanong, ‘Okay ka lang ba talaga?’ Nakakamiss toh talaga."

    # Start of flashback sequence
    scene clinic1 at Transform(xysize=(2580, 1520)) with fade
    show nurse_normal at right
    show Justine_normal at justine_bottom_left

    n "Ay dios mio, tambay ka nanaman dito uli? Ano nanaman pakiramdam mo mijo."

    show Justine_talking at justine_bottom_left
    jus "Wala po ma'am, unting sakit lang ng ulo po."

    
    n "Wag mo kalimutan na alagaan mo sarili mo mijo."

    # End of flashback
    scene clinic2 at Transform(xysize=(2580, 1520)) with fade
    show Justine_happy at justine_bottom_left

    jus "Ang bait talaga ni ma'am. Sana makadalaw ako ulit dito."

    jump floor1_right_hall
label sas:
    if not visited_sas:
        $ visited_sas = True

        scene bg_sas at Transform(xysize=(2580, 1520)) with fade
        show Justine_normal at justine_bottom_left with dissolve
        show Justine_talking at justine_bottom_left with dissolve
        jus "Yung SAS Office....."
        show Justine_sad at justine_bottom_left with dissolve
        jus "Hays.. Naalala ko tuloy tuwing enrollment"
        jus "Paunahan talaga"
        hide Justine_sad
        jump floor1_right_hall
    else:
        scene bg_sas at Transform(xysize=(2580, 1520)) with fade
        show Justine_happy at justine_bottom_left with dissolve
        jus "Buti nalang tapos na ako sa mga ganyan ganyan"
        hide Justine_happy
        jump floor1_right_hall
        return


label right_hall_forward2:
    scene bg_acad at Transform(xysize=(2580, 1520))  with fade
    call screen right_hall_menu1
    return
    # Move to a NEW hallway, not back to right_hall
    # or create another label like "deeper_hallway"

label show_documents:
    scene bg_acad at Transform(xysize=(2580, 1520))  with fade
    show doc1 with fade
    
    "This is the QR Code wherein you can scan thru phone"
    pause

    show doc2 with fade
    "Here is the second request letter template"

    pause

    show doc3 with fade

    "This is the third document for the campus reservation"

    pause

    show doc4 with fade
    "Lastly, this is the final version of the form"

    pause
    jump right_hall_forward2 


label director:
    scene bg_director at Transform(xysize=(2580, 1520))
    show Justine_normal
    show Justine_talking
    jus "Oh, ito yung director office"

    show Justine_normal
    show Justine_laughing
    jus "Hehe, naaalala ko laging busy si Direk"
    show Justine_happy
    jus "Para i-improve pa lalo yung Campus"

    show Justine_normal
    show Justine_laughing
    jus "Huwag na natin istorbohin si Direk.. (Justine said please)"
    hide Justine_normal
    hide Justine_laughing

    jump right_hall_forward2  



label admin:
    
    scene adminoffice at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left

    jus "Na-alala ko nung gumawa kami ng system para sa finals namin sa comprog"
    jus "pumunta kami dito para humingi ng permiso na mag-ikot sa campus at mag-picture"

    show Justine_Sighing at justine_bottom_left
    jus "naka-ilang balik kami dahil may proper procedure pala bago pumunta dito."

    # Start of flashback sequence
    scene lobbychairs at Transform(xysize=(2580, 1520)) with fade
    show Mae_talking at left
    show Sophie_normal at right
    m "Kaming dalawa nalang ni Sophie yung papasok sa loob para ipasa yung letter"

    # 1st Attempt
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Mae_smiling at left with dissolve
    show Sophie_smiling at right with dissolve
    "(Left the office after a few minutes)"
    hide Mae_smiling with dissolve
    hide Sophie_smiling 

    scene lobbychairs at Transform(xysize=(2580, 1520)) with fade
    show Sophie_talking at right 
    s "Guys ulitin daw mali raw yung format ng letter"
    hide Sophie_talking at right

    show Mae_talking at left 
    m "Ganito raw yung proper format"
    show Mae_holding_paper at left
    # 2nd Attempt
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Sophie_talking at right 
    show Mae_normal at left 
    "left the office after a few minutes"

    scene lobbychairs at Transform(xysize=(2580, 1520)) with fade
    show Mae_talking at left
    m "need naman daw ng appointment sa sinta"

    # 3rd Attempt
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Sophie_talking at right 
    s "Manifesting ma-approve na to"
    show Mae_normal at left
    "left the office after a few minutes"

    scene lobbychairs at Transform(xysize=(2580, 1520)) with fade
    show Mae_talking at right
    ma "Finally! na-approve na rin HAHAHAHA"
    hide Mae_talking
    # End of Flashback
    show Justine_laughing at justine_bottom_left
    jus "Haha... naaawa ako sa kanila"
    hide Justine_laughing 
    
    # ____CHOICES_____
    menu:
        "knock and enter the admin office":
            jump adm_office1
        "Just enter the door":
            jump adm_office2
    
    jump right_hall_forward2


label adm_office1:
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left
    jus "Hello po ma'am vidal"

    show Vidal_talking at right 
    v "And you are..?"

    show Justine_talking at justine_bottom_left
    jus "Justine po ma’am from BSIT 4-1"

    show Vidal_talking at right
    v "Oh why hello Justine, what can I do for you?"

    show Justine_talking at justine_bottom_left
    jus  " nag-iikot Ikot lang po para sa huling sandali ko as a student of this sintang paaralan"

    show Vidal_talking at right
    v "Kung ganon din ay, enjoyin mo na habang nandito ka"

    show Justine_talking at justine_bottom_left
    jus "Maraming salamat po"

    jump right_hall_forward2 

label adm_office2:

    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Vidal_talking at right
    v "Sino ka at bakit ka pumapasok lang ng basta basta?"
    show Justine_talking at justine_bottom_left
    jus "uhmmm... Justine ma’am from BSIT 4-1 po"
    show Vidal_angry_talking at right 
    v "Justine!!! Ilang taon ka nang nag-aaral dito pero hindi mo man lang alam ang tamang proseso bago pumasok?"
    show Justine_scared at justine_bottom_left
    jus "Sorry po Ma'am Vidal, hindi na po mau-ulit"

    show Vidal_angry_talking at right
    v "Kakatok ka lang ng 3 beses and give your greetings, ganoon ba kahirap yon?"

    show Justine_scared at justine_bottom_left 
    jus "Maraming salamat po"
    hide Justine_scared 

    show Vidal_angry_talking at right with dissolve
    v "Labas!, marmai pa kaming ginagawa at dadagdag ka pa!!!"

    scene adminoffice at Transform(xysize=(2580, 1520)) with fade
    "Justine was forced out"

    jump right_hall_forward2 


label mid:
    scene bg_midstair at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "grabe walang katao tao himala?"
    hide Justine_Sighing

label right_hall_forward3:
    scene bg_midstair at Transform(xysize=(2580, 1520)) with fade
    call screen right_hall_menu2

label lgbt_cr:
    scene bg_lgbt3 at Transform(xysize=(2580, 1520)) with fade
    scene bg_lgbt2 at Transform (xysize=(2580, 1520)) with fade
    scene bg_lgbt1 at Transform (xysize=(2580, 1520)) with fade
    show Justine_normal at justine_bottom_left
    show Justine_talking at justine_bottom_left
    jus "Nung nag PUPCET kami dati, nagulat ako na may LGBTQ na cr"
    jus "Kasi sa lahat ng school na napag-entrance exam ko"
    jus "Ngayon lang ako nakakita ng cr na para sa LGTBQ"
    
    show Justine_talking at justine_bottom_left
    show Justine_laughing at justine_bottom_left
    jus "Iba talaga ang PUP"
    hide Justine_talking
    hide Justine_laughing

    jump lgbt_cr_menu

label lgbt_cr_menu:
    scene bg_lgbt1 at Transform(xysize=(2580, 1520)) 
    call screen lgbt_cr

label garden_back:
    menu:
        "Back Garden and Greet the Guard":
            jump back_garden
        "Back Garden and Didn't Greet the GUard":
            jump back_garden_1

label back_garden:
    
    scene bg_garden
    show Justine_normal at justine_bottom_left 
    show Justine_talking at justine_bottom_left
    jus "Hmmmm, naaalala ko sa banda rito namin nilagay yung mga project na halaman"
    jus "Noong first year kami"
    hide Justine_normal 
    hide Justine_talking

    show Guard normal
    show Guard_talking_annoyed
    g "Oyyy oyy, bawal pumunta rito ng walang paalam"
    hide Guard normal
    hide Guard_talking_annoyed

    show Justine_normal at justine_bottom_left
    show Justine_talking at justine_bottom_left
    jus "Ahhh sige po kuya, alis na lang ako"
    hide Justine_normal
    hide Justine_talking

return
label back_garden_1:
    scene bg_garden at Transform(xysize=(2580, 1520))
    scene g1 at Transform(xysize=(2580, 1520))
    scene g2 at Transform(xysize=(2580, 1520))
    scene g3 at Transform(xysize=(2580, 1520))
    scene g4 at Transform(xysize=(2580, 1520))
    scene g5 at Transform(xysize=(2580, 1520))
    scene g6 at Transform(xysize=(2580, 1520))
    scene g7 at Transform(xysize=(2580, 1520))
    scene g8 at Transform(xysize=(2580, 1520)) 
    show Justine_normal at justine_bottom_left 
    jus "Hmmmm, naaalala ko banda rito namin nilagay yung mga project na halaman"
    jus "Noong first year kami"
    hide Justine_normal

    show Guard annoyed at right
    g "Ang kulit mo ah! Diba sinabi ko na bawal dito?!"
    hide Guard annoyed

    show Justine_normal at justine_bottom_left 
    jus "Sorry po kuya, promise hindi na po mauulit"
    hide Justine_normal

    show Guard annoyed
    g "Talagang hindi na mau-ulit to"
    g "Dahil dadalhin na kita sa Admin Office"
    hide Guard annoyed

    show Justine_normal at justine_bottom_left 
    jus "Sorry po talaga kuya, hindi na talaga to uulit promise"
    jus "Gusto ko lang naman pong mag-ikot"
    hide Justine_normal

    show Guard annoyed at right
    g "Magpaliwanag ka nalang sa Admin Office"
    hide Guard annoyed

    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Guard annoyed at right
    g "Good morning po Ma'am, irereklamo ko lang po ito"
    g "Paulit-ulit na kasi at hindi sumusunod"
    g "Pumupunta sa mga lugar na hindi dapat puntahan ng walang permiso"
    hide Guard annoyed

    show Vidal_normal at right
    show Vidal_talking at right
    v "Ano pangalan, year at section mo iho?"
    hide Vidal normal
    hide Vidal_talking

    show Justine_normal at justine_bottom_left 
    show Justine_talking at justine_bottom_left
    jus "Justine po and BSIT 4-1"
    hide Justine_normal
    hide Justine_talking

    show Vidal_normal at right
    show Vidal_talking at right
    v "Okay Justine, is that true?"
    hide Vidal_normal
    hide Vidal_talking

    show Justine_normal at justine_bottom_left
    show Justine_talking at justine_bottom_left
    jus "Pasensya na po Ma'am"
    jus "Gusto ko lang naman po mag-ikot"
    hide Justine_normal
    hide Justine_talking 

    show Vidal_normal at right
    show Vidal_talking at right
    v "Dahil diyan magkakaroon ka ng punishment dahil sa hindi pagsunod at paglabag"
    v "Kinakailangan mo na gawin ang mga dapat na i-utos o i-aassign sayong gawain"
    v "Kailangan mo itong matapos at magawa kung hindi malalate ang pag-graduate mo"
    hide Vidal_normal
    hide Vidal_talking

    show Justine_talking at justine_bottom_left 
    show Justine_Sighing at justine_bottom_left 
    show Justine_scared at justine_bottom_left 
    jus "Pero po Ma'am...."
    hide Justine_talking
    hide Justine_Sighing
    hide Justine_scared

    show Vidal_normal at right
    show Vidal_angry at right
    show Vidal_angry_talking at right
    v "No more buts, you may go now"
    hide Vidal_normal
    hide Vidal_angry
    hide Vidal_angry_talking

    "THE END"

    jump right_hall_forward3

label garden_1:
    scene bg_garden at Transform(xysize=(2580, 1520)) with fade 
    
label garden_view_menu:
    scene bg_garden at Transform(xysize=(2580, 1520))
    call screen garden_view

label garden_view_menu1:
    scene bg_garden1 at Transform(xysize=(2580, 1520))
    call screen cat
label garden_view2:

    scene bg_garden2 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_garden3 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
         
    jump back_garden_view

label back_garden_view:
    scene bg_garden3 at Transform(xysize=(2580, 1520))
    call screen back_garden


label g:
    scene g1 at Transform(xysize=(2580, 1520))
    scene g2 at Transform(xysize=(2580, 1520))
    scene g3 at Transform(xysize=(2580, 1520))
    scene g4 at Transform(xysize=(2580, 1520))
    scene g5 at Transform(xysize=(2580, 1520))
    scene g6 at Transform(xysize=(2580, 1520))
    scene g7 at Transform(xysize=(2580, 1520))
    scene g8 at Transform(xysize=(2580, 1520)) 
    scene g9 at Transform(xysize=(2580, 1520))
    scene g10 at Transform(xysize=(2580, 1520))
    scene g11 at Transform(xysize=(2580, 1520))
    scene g12 at Transform(xysize=(2580, 1520))
    call screen entrance_hideout
    return
 

label right_exit:
    scene bg_exit1 at Transform(xysize=(2580, 1520)) with fade
    scene bg_exit2 at Transform(xysize=(2580, 1520)) with fade
    scene bg_exit3 at Transform(xysize=(2580, 1520)) with fade
    scene bg_exit4 at Transform(xysize=(2580, 1520)) with fade
    scene bg_exit5 at Transform(xysize=(2580, 1520)) with fade
    show Justine_normal at justine_bottom_left 
    show Justine_talking at justine_bottom_left
    jus "Ohhh.. ito yung short cut palabas sa gate"
    jus "Pero usually kasi naka-sara to."
    hide Justine_normal at justine_bottom_left
    hide Justine_talking at justine_bottom_left

    menu:
        "Pet the Cat": # _____Choice 1_______
            jump pet_cat
        "Do not Pet the Cat":
            jump donotpet
        "Proceed to the Main Gate":
            jump maingate
      
label pet_cat:
    scene pet_cat at Transform(xysize=(2580, 1520)) with fade
    show Justine_normal at justine_bottom_left 
    show Justine_laughing at justine_bottom_left 
    jus "Wow! Ang cute naman ng pusa"
    hide Justine_normal
    hide Justine_laughing

    jump right_exit_menu

label donotpet:
    scene bg_exit5 at Transform(xysize=(2580, 1520)) with fade
    jump right_exit_menu

label maingate:
    scene bg_after_school_gate at Transform(xysize=(2580, 1520)) with fade
    show Justine_normal at justine_bottom_left 
    show Justine_laughing at justine_bottom_left 
    jus "ang daming ko naging memorya dito"
    jus "may maganda pero may mga part na gusto ko din kalimutan"
    jus "pero masasabi ko talaga na ma mi-miss ko talaga to sa sususnod ulit sintang paaralan"
    "THE END"
    jump outside_exit_menu
label right_exit_menu:
    scene bg_exit6 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit7 at Transform(xysize=(2580, 1520)) with fade
    call screen right_exit_menu1

label outside_exit:    
    scene bg_exit8 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit9 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit10 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    jump outside_exit_menu

label fire_exit_inside1:
    scene bg_fire_exit_inside1 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside2 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside3 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside4 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside5 at Transform(xysize=(2580, 1520)) with fade

label fire_exit_inside_menu:
    scene bg_fire_exit_inside5 at Transform(xysize=(2580, 1520)) with fade
    call screen fire_exit_inside_menu1


label outside_exit_menu:
    scene bg_after_school_gate at Transform(xysize=(2580, 1520)) with fade
    call screen nav_door_gate
    
label upstairs:
    scene bg_stair1 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_stair2 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_stair3 at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "Ba yan! Wait nga!"
    
    hide Justine_Sighing

    jump second_floor_stair

label second_floor_stair:
    scene bg_stair4 at Transform(xysize=(2580, 1520)) with fade
    scene bg_stair5 at Transform(xysize=(2580, 1520)) with fade
    jump second_floor_stair1

label second_floor_stair1:
    scene bg_stair6 at Transform(xysize=(2580, 1520)) with fade
    call screen fire
    return

label male_bathroom1:
    scene m1 at Transform(xysize=(2580, 1520)) with fade
    scene m2 at Transform(xysize=(2580, 1520)) with fade
    scene m3 at Transform(xysize=(2580, 1520)) with fade
    scene m4 at Transform(xysize=(2580, 1520)) with fade
    scene m5 at Transform(xysize=(2580, 1520)) with fade
    call screen male_bathroom
    return

label fire_exit:

    if not visited_fire_exit:
        $ visited_fire_exit = True

        scene fire_exit2 at Transform(xysize=(2580, 1520)) with fade
        show justine_talking at justine_bottom_left
        show Justine_happy at justine_bottom_left 
        jus "Na-aalala ko rito lagi pumupunta si Mae"
        jus "Tuwing nag-aantay kami sa last subject"
        hide Justine_talking
        hide Justine_happy
        # Start of Flashback Scene____
        scene fire_exit1 at Transform(xysize=(2580, 1520)) with fade
        show Mae_smiling 
        show Mae_talking 
        m "grabe ang sarap ng hangin"
        m "nakaka relax pwede ka mag emote dito oh hahaha"
        hide Mae_smiling
        hide Mae_talking 
        # End of Flashback
    else:
        # IRL
        show Justine_smiling at justine_bottom_left 
        show Justine_happy at justine_bottom_left
        jus "hmmm.. Nakakrelax nga"

        # Justine Monologue
        jus "Pero alis na tayo rito kasi hindi dapat tinatambayan 'to"
        hide Justine_smiling
        hide Justine_happy
        # End of Justine Monologue  
    jump second_floor_menu


label second_floor_menu:
    scene bg_floor2_halfwayright at Transform(xysize=(2580, 1520)) with fade
    call screen right_hall_menu3

label floor2_1:
    scene sf1 at Transform(xysize=(2580, 1520)) with fade
    scene sf2 at Transform(xysize=(2580, 1520)) with fade
    scene sf3 at Transform(xysize=(2580, 1520)) with fade
    scene sf4 at Transform(xysize=(2580, 1520)) with fade
    scene sf5 at Transform(xysize=(2580, 1520)) with fade
    scene sf6 at Transform(xysize=(2580, 1520)) with fade
    call screen room
    return

label floor2_2:
    scene sf6 at Transform(xysize=(2580, 1520)) with fade
    call screen room
    return


label room_204:

    if not visited_room_204:
        $ visited_room_204 = True

        scene chair at Transform(xysize=(2580, 1520)) with fade
        show Justine_happy at justine_bottom_left 
        show Justine_talking at justine_bottom_left 
        jus "madami akong memory dito"
        jus "ang pinaka paborito ko siguro yung nag pra-practice kami para sa chorale"
        
        show Justine_happy at justine_bottom_left
        jus "Na-aalala ko tuloy si Carl nung huling practice namin"
        show Justine_laughing at justine_bottom_left
        hide Justine_happy
        hide Justine_laughing

        # Start of the Flashback
        scene chair1 at Transform(xysize=(2580, 1520)) with fade
        show Carl_suggesting at kim_bottom_right 
        c "kabayo ay di natin problema~  pulot at damo lang ay tama na~"
        show Carl_talking
        hide Carl_suggesting
        hide Carl_talking
        # End of Flashback
    else:
        # IRL
        show Justine_happy at justine_bottom_left 
        jus "Kahit 2 days lang practice namin na-clutch pa rin namin"
        show Justine_laughing at justine_bottom_left 
        hide Justine_happy
        hide Justine_laughing

    jump floor2_2

label floor2_3:
    scene sf7 at Transform(xysize=(2580, 1520)) with fade
    call screen pup
    return
label pup_library:

    if not visited_pup_library:
        $ visited_pup_library = True
        scene library1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left with dissolve 
        jus "Dito sa library na 'to"
        show Justine_happy at justine_bottom_left 
        jus "Naaalala ko lagi kaming nag-tatambay dito"
        jus "Kapag may vacant time o kaya kapag nags-study kami rito"
        show Justine_talking at justine_bottom_left
        jus "na alala ko tuloy yung sinabi ni jorie"
        hide Justine_talking
        hide Justine_happy
        # Start of the Flashbacks

        scene library1 at Transform(xysize=(2580, 1520)) with fade
        show Sophie_smiling
        s "At sobrang lamig sa room nato dahil may aircon kaya ang ganda tambayan."
        show Sophie_talking 
        s "Lalo na kung sa room namin pag mag klase ang init"
        s "kaya after ng klase namin punta agad sa library."
        hide Sophie_smiling
        hide Sophie_talking
        # End of flashback

        show Justine_happy at justine_bottom_left 
        jus "Justine: well, totoo naman malamig dito"
        show Justine_talking at justine_bottom_left 
        jus "at pwede ka din humiram ng libro para pang palipas oras din"
        hide Justine_happy
        hide Justine_talking
        
    else:
        scene library2 at Transform(xysize=(2580, 1520)) with fade
        show Justine_happy at justine_bottom_left 
        jus "Tambayan at Studyhan namin dito" 
        show Justine_talking at justine_bottom_left
        hide Justine_talking
        hide Justine_happy
        return

    jump floor2_3

    
label floor_1:
    scene sf7 at Transform(xysize=(2580, 1520)) with fade
    scene sf8 at Transform(xysize=(2580, 1520)) with fade
    scene sf9 at Transform(xysize=(2580, 1520)) with fade
    scene sf10 at Transform(xysize=(2580, 1520)) with fade
    scene sf11 at Transform(xysize=(2580, 1520)) with fade
    scene sf12 at Transform(xysize=(2580, 1520)) with fade
    scene sf13 at Transform(xysize=(2580, 1520)) with fade
    call screen discussion
    return

label discussion_room:
    scene discussion at Transform(xysize=(2580, 1520)) with fade
    show Justine_normal at justine_bottom_left 
    jus "Pagkakatanda ko, pwede tong room na to"
    show Justine_talking at justine_bottom_left
    jus "Basta magpapaalam lang sa librarian"
    hide Justine_happy at justine_bottom_left
    hide Justine_talking at justine_bottom_left

    jump floor_2

label floor_2:
    scene sf13 at Transform(xysize=(2580, 1520)) with fade
    call screen discussion
    return

label floor__1:
    scene sf14 at Transform(xysize=(2580, 1520)) with fade
    scene sf15 at Transform(xysize=(2580, 1520)) with fade
    scene sf16 at Transform(xysize=(2580, 1520)) with fade
    scene sf17 at Transform(xysize=(2580, 1520)) with fade
    call screen second_last_floor
    return

label floor__2:
    scene sf17 at Transform(xysize=(2580, 1520)) with fade
    call screen second_last_floor
    return
label second_floor:
    scene bg_second_floor at Transform(xysize=(2580, 1520)) 
    call screen second_floor_menu

label halfwayground:
    scene left_halfway_ground1 at Transform(xysize=(2580, 1520)) with fade
    call screen left_halfway_menu


label nstp:
    scene bg_nstp with fade
    call screen nstp_room
    return


label faculty_lounge:
    scene faculty_inside at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left with dissolve
    show Justine_normal at justine_bottom_left
    jus "Ang tagal ko ring hindi nakatapak dito sa faculty… pero parang walang nag bago."

    show Justine_happy at justine_bottom_left
    jus "Dito ako laging nakatambay."
    jus "Dito ako palagi nakikiusap sa professor namin nung Discrete Structures para makapa consult sa project."

    show Justine_laughing at justine_bottom_left
    jus "Minsan, nakikipag kwentuhan o nakiki chismis lang pagkatapos ng klase."
    hide Justine_laughing at justine_bottom_left

    # Start of flashback
    "(Flashback Sequence)"
    show Faculty_normal
    show Faculty_talking
    "Yan naman, nakalimutan mo pa kasi ipasa yung assignment mo."
    show Faculty_normal
    show Faculty_talking
    "Swerte ka na pagbibigyan kita dito ah," 
    show Faculty_normal
    show Faculty_talking
    "wag mo naman kalimutan sa susunod ha?"
    hide Faculty_normal
    hide Faculty_talking

    show Justine_talking at justine_bottom_left
    jus "Opo ma'am, pasensya na."
    show Justine_scared at justine_bottom_left

    show Justine_sad at justine_bottom_left
    show Justine_talking at justine_bottom_left 
    jus "Ramdam ko pa din ‘yung kaba tuwing kumakatok ako sa pinto." 
    jump left_ground_2
label left_ground1:
    scene left_halfway_ground1 at Transform(xysize=(2580, 1520)) with fade
    scene left_halfway_ground2 at Transform(xysize=(2580, 1520)) with fade 
    call screen left_ground_menu1

label left_ground_1:
    scene left_halfway_ground2 at Transform(xysize=(2580, 1520)) with fade 
    call screen left_ground_menu1
    return
label left_hallway_menu:


label left_ground2:
    scene left_halfway_ground3 at Transform(xysize=(2580, 1520)) with fade
    scene left_halfway_ground4 at Transform(xysize=(2580, 1520)) with fade
    scene left_halfway_ground5 at Transform(xysize=(2580, 1520)) with fade
    call screen left_ground_menu2
    return

label left_ground_2:
    scene left_halfway_ground5 at Transform(xysize=(2580, 1520)) with fade
    call screen left_ground_menu2
    return

label avr_room:
    scene bg_avr_door at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left

    jus "Ah, yung AVR... Naalala ko si Sophie tuloy. Na high blood pa siya noon dahil pinalinis pa siya nung nakalat namin yung AVR..."

    # Start of flashback
    scene bg_avr with fade
    show Sophie_angry at right
    show Justine_shocked at justine_bottom_left 

    soph "Ano ba yan, itatapon nalang eto! Mas lalo na ikaw Justin! Lagot ka sa akin mamaya!"

    # End of flashback
    scene bg_avr with fade
    show Justine_shivering at justine_bottom_left

    jus "Inabangan niya pa ako sa gate nung uwian... Nakakaiba talaga yung galit netong babae na 'to…"

    jump left_ground_3

label left_ground3:
    scene left_halfway_ground6 at Transform(xysize=(2580, 1520)) with fade
    scene left_halfway_ground7 at Transform(xysize=(2580, 1520)) with fade
    call screen left_ground_menu3
    return

label left_ground_3:
    scene left_halfway_ground7 at Transform(xysize=(2580, 1520)) with fade
    call screen left_ground_menu3
    return

label third1:
    scene stair1 at Transform(xysize=(2580, 1520)) with fade
    scene stair2 at Transform(xysize=(2580, 1520)) with fade
    scene stair3 at Transform(xysize=(2580, 1520)) with fade
    scene stair4 at Transform(xysize=(2580, 1520)) with fade
    scene stair5 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor1
    return
label third1_1:
    scene stair5 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor1
    return

label thirdfloor_hall:
    scene hallway1 at Transform(xysize=(2580, 1520)) with fade

label room_302:

    if visited_room_302:

        $ visited_room_302
        scene room1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left 
        jus "Room 302…"
        show Justine_laughing at justine_bottom_left 
        jus "naalala ko tuloy yung nangyari dati hahaha"
        hide justine_talking
        hide Justine_laughing

        # Start of the Flashback
        scene room2 at Transform(xysize=(2580, 1520)) with fade
        show Kim_calling at right with dissolve
        k "Nasaan kayo guys? (nag-call sa gc)"
        hide Kim_calling

        show Justine_holding_phone at justine_bottom_left 
        jus "Nasa room 303 po"
        hide Justine_holding_phone

        "(After a few minutes, Kim entered the room a bit irritated)"

        show Kim_normal at right 
        hide Kim_normal

        show Carl_talking at left 
        c "Ay… room 303 kase nakalagay sa table eh"
        hide Carl_talking

        show Kim_talking at right 
        k "Pagsilip ko sa room 303 te"
        show Kim_normal at right 
        k "ibang estudyante nakita ko tas nakatitigan ko pa."
        k "Nakakahiya.."
        hide Kim_talking
        hide Kim_normal
    else:
        scene room1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_laughing at justine_bottom_left
        jus "Yung table talaga may kasalanan"
        hide Justine_laughing

    jump turn_right_4

label room_305:
    scene room307_2 at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left 
    jus "Room 305… ilang klase rin natin dito ginanap."
    hide Justine_talking

    show Mae_talking at right 
    ma "Oo, dito ako unang na tawag sa graded recitation"
    hide Mae_talking

    show Mae_smiling at right 
    ma "wala pa akong review noon. Haha."
    hide Mae_smiling

    show Justine_alarmed at justine_bottom_left 
    jus "Oh Mae andito ka pala"
    hide Justine_alarmed 

    show Mae_smiling at right
    ma "Oo HAHAHA"
    hide Mae_smiling 

    show Justine_Sighing at justine_bottom_left
    jus "Naalala ko rin ‘yung lecture na walang kuryente."
    show Justine_happy at justine_bottom_left 
    jus "Ang init, pero tuloy pa rin."
    show Justine_laughing at justine_bottom_left
    jus "‘Yun ang tunay na dedication"
    hide Justine_laughing
    hide Justine_happy
    hide Justine_Sighing

    menu:
        "Peek through the Window":
            jump peek_window
        "Walk away":
            jump walk_away1
    jump turn_right_2
label peek_window:
    "Justine looks through the glass window in the door"

    show Justine_talking at justine_bottom_left 
    jus "Parang hindi na siya kasing gulo gaya nung dati"
    hide Justine_talking

    show Mae_talking at right with dissolve
    ma "Oo. Pero kahit paano, may sentimental value pa rin."
    hide Mae_talking

    jump turn_right_2



label walk_away1:

    scene hallway3 at Transform(xysize=(2580, 1520)) with fade
    "Justine smiles faintly and continues walking down the hallway."
 
    show Justine_waving at justine_bottom_left
    jus "Salamat, Room 305."
    hide Justine_waving

    show Justine_sad at justine_bottom_left
    jus "Kahit minsan stressful, naging parte ka ng journey."
    hide Justine_sad

    show Mae_talking at right
    ma "Sige na nga"
    hide Mae_talking


    show Mae_smiling at righ with dissolve
    ma "Baka maiyak pa tayo riyan"
    hide Mae_smiling

    jump turn_right_2
label room_307:
    "(Pumasok si Justine sa ROOM 307)"

    scene room307_1 at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left
    jus " ayy naalala ko tong room na ‘to."
    hide Justine_talking

    show Justine_happy at justine_bottom_left
    jus "Ito yung isa sa mga room na ‘di ko makalimutan."
    hide Justine_happy

    scene room307_3 at Transform(xysize=(2580, 1520)) with fade
    show Justine_laughing at justine_bottom_left
    jus "dito kami nagpatay ng oras para sa PE namin hahaha."
    hide Justine_laughing

    show Justine_Sighing at justine_bottom_left 
    jus "Tapos wala palang klase"
    hide Justine_Sighing

    show Justine_disappointed at justine_bottom_left 
    jus "Prinactice pa naman namin mga excercises namin."
    hide Justine_disappointed

    jump turn_right_1

label turn_right_2:
    scene hallway3 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor3
    return
label boys_cr:
    scene m1 at Transform(xysize=(2580, 1520)) with fade
    scene m2 at Transform(xysize=(2580, 1520)) with fade
    scene m3 at Transform(xysize=(2580, 1520)) with fade
    scene m4 at Transform(xysize=(2580, 1520)) with fade
    scene m5 at Transform(xysize=(2580, 1520)) with fade
    "(Pumasok si Justine sa boys' CR)"

    show Justine_scared at justine_bottom_left
    "Amoy linis pero may halong luma—parang floor wax na natuyuan ng pawis."
    show Justine_smiling at justine_bottom_left 
    jus "Yung salamin, andito pa rin."
    show Justine_talking at justine_bottom_left 
    jus "At mga urinal wala paring pagbabago. Classic."
    show Justine_laughing at justine_bottom_left 
    jus "Dito ako minsang nagtago noon. Para makapag isip isip."
    hide Justine_smiling
    hide Justine_talking
    hide Justine_laughing
    hide Justine_scared

    call screen boy_bathroom
label turn_right:
    scene hallway1 at Transform(xysize=(2580, 1520)) with fade
    scene hallway2 at Transform(xysize=(2580, 1520)) with fade

label turn_right_1:
    scene hallway2 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor2
    return

label girls_cr:
    if not visited_girls_cr:

        $ visited_girls_cr = True
        scene girls1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left 
        jus "hmm? Eto yung CR for girls, ano kaya itsura neto sa loob?"
        hide Justine_talking

        show Justine_laughing at justine_bottom_left 
        jus "naalala ko tuloy yung sinabi ni Lyn"
        hide Justine_laughing

        # Start of the Flashback
        scene girls2 at Transform(xysize=(2580, 1520)) with fade
        show Lyn_talking at right
        l "ano itsura ng cr ng boys justine?"
        show Lyn_smug at right
        l "Kasi samin may salamin na may tubig pa yung sa inyo?"
        hide Lyn_talking
        hide Lyn_smug
        # End of Flashback
    else:
        # IRL
        scene girls1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_realised at justine_bottom_left 
        jus "na-curious tuloy ako ano itsura ng loob"
        hide Justine_realised

        "Ella suddenly appear"
        show Ella_talking at right 
        e "huyy, ano ginagawa mo dyan?"
        show Ella_smiling at right 
        e "Bat ka nakatitig sa cr?"
        hide Ella_talking
        hide Ella_smiling

        show Justine_alarmed at justine_bottom_left 
        jus "Hu-huh?"
        show Justine_Sighing at justine_bottom_left 
        jus "Kung ano man ang iniisip mo mali yun"
        show Justine_talking at justine_bottom_left 
        jus "na alala ko lang yung sinabi ni Lyn tungkol sa CR ng girls"
        hide Justine_alarmed
        hide Justine_Sighing
        hide Justine_talking

        show Ella_grinning at right 
        e "ayy!"
        hide Ella_grinning

        show Ella_talking at right 
        e "Speaking of cr ng girls"
        hide Ella_talking

        show Ella_whispering at right 
        e "alam mo ba…"
        hide Ella_whispering

        show Ella_talking at right 
        e "kasi one time, mag isa lang akong pumunta"
        hide Ella_talking 

        show Ella_whispering at right 
        e " tas may nafeel ako na kakaiba"
        e "kaya sumilip ako"
        hide Ella_whispering

        show Ella_grinning at right
        e "sa door ng cr tas wala naman tas pag tingin ko ulit…"
        hide Ella_grinning
        
        show Justine_scared at justine_bottom_left
        jus "ta-tapos…?"
        hide Justine_scared

        show Ella_whispering at right 
        e "…si Lyn lang pala "
        hide Ella_whispering

        show Ella_grinning at right 
        e "kala mo nakakatakot noh"
        hide Ella_grinning

        show Ella_smiling at right 
        e "kala ko rin e hahahah"
        hide Ella_smiling

        show Justine_Sighing at justine_bottom_left 
        jus "hayss ano ba yan"
        hide Justine_Sighing

        show Justine_laughing at justine_bottom_left 
        jus "akala ko kung ano na hahaha…"
        hide Justine_laughing

        show Ella_talking at right 
        e "well anyway alis na ako may pupuntahan pa ako"
        hide Ella_talking

        show Justine_waving at justine_bottom_left 
        jus "ok bye"
        hide Justine_waving

    jump third1_1

label turn_right1:
    scene hallway4 at Transform(xysize=(2580, 1520)) with fade
    scene hallway5 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor6
    return

label turn_right_3:
    scene hallway5 at Transform(xysize=(2580, 1520)) with fade 
    call screen third_floor6
    return

label turn_right_4:
    scene hallway6 at Transform(xysize=(2580, 1520)) with fade 
    call screen third_floor4
    return

label turn_right5:
    scene hallway7 at Transform(xysize=(2580, 1520)) with fade
    scene hallway8 at Transform(xysize=(2580, 1520)) with fade
    scene hallway9 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor5
    return

label turn_right_5:
    scene hallway9 at Transform(xysize=(2580, 1520)) with fade
    call screen third_floor5

label science_lab:
    scene science_lab at Transform(xysize=(2580, 1520)) with fade
    call screen science_lab1
    return

label turn_left:
    scene rightside_staircase at Transform(xysize=(2580, 1520)) with fade
    call screen turn_left_1
    return

label fourth_floor:
    scene 1 at Transform(xysize=(2580, 1520)) with fade
    scene 2 at Transform(xysize=(2580, 1520)) with fade
    scene 3 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth_floor1
    return
label fourth_floor_1:
    scene 3 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth_floor1
    return
label m_bathroom:
    scene m1 at Transform(xysize=(2580, 1520)) with fade
    scene m2 at Transform(xysize=(2580, 1520)) with fade
    scene m3 at Transform(xysize=(2580, 1520)) with fade
    scene m4 at Transform(xysize=(2580, 1520)) with fade
    scene m5 at Transform(xysize=(2580, 1520)) with fade
    call screen ma_bathroom
    return

label fourth_floors1:
    scene f1 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth
    return

label comlab:
    if not visited_comlab:
        $ visited_comlab = True
        scene comlab at Transform(xysize=(2580, 1520)) with fade
        show Justine_alarmed at justine_bottom_left 
        jus "Ay! naalala ko bigla"
        jus "nung first time pa lang namin pumasok dito"
        jus "nung freshman pa lang kami"
        hide Justine_alarmed
        
        show Justine_laughing at justine_bottom_left 
        jus "nakita ko si carl binuksan yung pc at nagdrawing ng pasimple."
        hide Justine_laughing

        #Flashback
        show Justine_talking at justine_bottom_left 
        jus "Uy carl ano ginagawa mo?"
        hide Justine_talking

        show Carl_talking at right
        c "shhh wag kang maingay, mamaya makita tayo ni sir"
        hide Carl_talking
    else:
        show Justine_laughing at justine_bottom_left 
        jus "grabe ang tapang talaga nya hahaha…"
        hide Justine_talking

    jump fourth_floors1

label computer_hardware:
    scene comhardware at Transform(xysize=(2580, 1520)) with fade 
    show Justine_talking at justine_bottom_left 
    jus "Dito kami pumupunta kapag may hands on activity"
    jus "ang maintenance at repair ng mga equipment dito lalo na pag computer."
    hide Justine_talking 

    show Justine_happy at justine_bottom_left 
    jus "Naalala ko tuloy dati si Ella"
    jus " Halos sya lang ang naka ayos ng mga computer na pinapaayos sa amin noon"
    hide Justine_happy

    jump fourth_floors1

label project_proposal:
    if not visited_project_proposal:
        $ visited_project_proposal = True
        scene proj at Transform(xysize=(2580, 1520)) with fade 
        show Justin_talking at justine_bottom_left 
        jus "Dito kami pumunta nung nag project defense kami"
        hide Justin_talking

        show Justine_scared at justine_bottom_left 
        jus "Naalala ko grabe yung kaba ko nung proposal defense"
        jus "pero mas malala parin yung kaba ni Mae non"
        jus "hanggang ngayon hindi ko parin nalilimutan."
        hide Justine_scared

        # flashback
        show Justine_talking at justine_bottom_left 
        jus "Mae try mo kumalma, nanginginig kana"
        hide Justine_talking

        show Mae_talking at justine_bottom_left 
        m "Tinatry ko ok?"
        m "Pero what if ma-reject yung proposal?"
        m "What if ma blanko ako? What if-"
        hide Mae_talking
    else:
        show Justin_laughing at justine_bottom_left 
        jus "Grabe ang pag overthink nya"
        jus "halos nanginginig buong katawan nya noon HAHAHAHA"
        hide Justin_laughing

    jump fourth_floors2


label lab_management:
    if not visited_lab_management:
        $ visited_lab_management = True
        scene lab_management at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left 
        jus "Pagkakaalam ko dito nagluluto ang mga HM"
        jus "Lagi akong nagugutom sa tuwing napapadaan ako dito"
        jus "lalo na pag nagluluto ang mga HM"
        hide Justine_talking
    else:
        scene lab_management at Transform(xysize=(2580, 1520)) with fade
        show Justine_realised at justine_bottom_left 
        jus "Ohh IT lab"
        hide Justine_realised

        show Justine_talking at justine_bottom_left 
        jus "Ito yung admin or control room "
        jus "para sa lahat ng IT-related laboratories sa campus tulad ng Comlab"
        hide Justine_talkingshow Justine_talking
        jus "Ito yung admin or control room "
        jus "para sa lahat ng IT-related laboratories sa campus tulad ng Comlab"
        hide Justine_talking

        show Justine_sad at justine_bottom_left 
        jus "pero until now di pa rin ako nakakapasok dyan."
        hide Justine_sad

        show Lyn_pout at right
        l "actually same"
        hide Lyn_pout

        show Justine_alarmed at justine_bottom_left 
        jus "WAH!! Lyn?! San ka nanggaling?"
        hide Justine_alarmed

        show Lyn_talking at right
        l " i-kalma mo tih hahaha, may pinapakuha lang sakin na drive si kim "
        hide Lyn_talking

        show Justine_talking at justine_bottom_left 
        jus "ah oo nga pala may nabanggit nga na ganyan si kim kanina"
        jus "pero grabe ka naman bat bigla bigla ka sumusulpot?"
        hide Justine_talking

        show Lyn_Anya_smirk at right
        l "sorry na HAHAHAHA"
        l "Anyway, bye, kukunin ko pa yung drive"
        hide Lyn_Anya_smirk

        show Justine_waving at justine_bottom_left 
        jus "bye "
        hide Justine_waving

        jump kitchen_lab

label food_beverage:
    scene food_and_bev_room2 at Transform(xysize=(2580, 1520)) with fade 
    if not visited_food_beverage:
        $ visited_food_beverage = True
        scene s
        show Justine_talking at justine_bottom_left 
        jus "Pag napapadaan ako rito"
        jus "feel ko lagging may birthday dahil sa ganda ng pagkakaayos"
        jus "naalala ko yung sinabi ni Jorie tungkol sa room na to"
        hide Justine_talking
        # Flashback
        show Jorie_talking at right
        j "Kaya pala ganyan"
        j "ang ayos nyan kase dyan nag t-training ang mga HM Students"
        hide Jorie_talking

        show Jorie_smiling at right
        j "kung ano nga ba ang dapat nilang gawin pag sila ay natatrabaho na."
        hide Jorie_smiling
    else:
        show Justine_talking
        jus "feel ko ang intense ng training nila dyan"
        hide Justine_talking
 
    jump fourth_floors3
label kitchen_lab:
    scene kitchen_lab2 at Transform(xysize=(2580, 1520)) with fade 

    show Justine_talking at justine_bottom_left 
    jus "Kung may storage room sila, syempre may kitchen din"
    hide Justine_talking

    show Lyn_talking
    l "Dito naman nagluluto ang mga HM Students kaya pag napapadaan ako rito"
    l "nagugutom agad ako dahil sa bango ng mga niluluo nila."
    hide Lyn_talking

    show Justine_alarmed at justine_bottom_left 
    jus "TALAGA NAMAN LYN ??"
    jus "BIBIGYAN MO BA AKO NG SAKIT SA PUSO?"
    hide Justine_alarmed

    show Lyn_talking at right
    l "HAHAHA… SORRRY NA ANYWAY BABALIK NA SANA  AKO KASO NA KITA KITA MYBAD"
    l "Minsan gusto ko nalang tumayo dyan nang matagal"
    l "dahil di nakakasawang amuyin ang mga niluluo nila"
    hide Lyn_talking

    show Justine_talking at justine_bottom_left 
    jus "sa totoo lang"
    hide Justine_talking

    show Lyn_talking at right
    l "anyway bibigay ko papala tong drive kay kim"
    l "Bye~"

    jump fourth_floors3

label HM_storage:
    scene hm_storage_room1 at Transform(xysize=(2580, 1520)) with fade 
    show Justine_happy at justine_bottom_left 
    jus "Ang ganda talaga rito."
    jus "Andito yung mga plato,baso, at uniform na ginagamit ng mga HM Students."
    jus "Pag nakikita ko nga silang may dalang lutong pagkain ay naiinggit ako"
    jus "kase akala ko dati puro lang sila linis"
    jus "yung parang mga House keeping yun pala may halong pagkain din"
    hide Justine_happy

label student_org:
    if not visited_org:
        $ visited_org = True
        scene student_org1 at Transform(xysize=(2580, 1520)) with fade  
        show Justine_talking at justine_bottom_left 
        jus "Hmm, org room"
        jus "eto yung room na ginagamit nila pag kaylangan ng mga org."
        jus "Andito din mga gamit ng iba’t ibang org."
        jus "naalala ko sabi ni Ella nung first year kami"
        hide Justine_talking
    else:
        show Justine_talking at justine_bottom_left 
        jus "grabe, ang strict talaga ng school na ito"
        hide Justine_talking

label housekeeping_room:
    if not visited_housekeeping_room:
        $ visited_housekeeping_room = True
        scene housekeeping_room at Transform(xysize=(2580, 1520)) with fade  
        show Justine_talking at justine_bottom_left 
        jus "Housekeeping Room."
        jus "Parang ilang beses ko nang nadadaanan"
        jus "‘to pero never ko pa rin siya napapasok"
        jus "Naalala ko yung sabi ni Mae dati…"

        #flashback
        show Justine_smiling at justine_bottom_left 
        jus "Para saan kaya ‘to?"
        hide Justine_smiling

        show Mae_talking 
        m "Ah, ‘yan?"
        m "Diyan raw nagpa-practice yung HM students ng mga housekeeping tasks"
        m "like bed making, towel folding, at room cleaning."
        m "Parang mini-hotel room training area."
        m "May mga gamit d’yan like mop, linen, tsaka mga hotel-grade supplies."
        m "Parang combo siya ng storage at simulation room."
        m "Hindi halata, pero malaking tulong ‘to sa training nila"
        m "Diyan nila natututunan ‘yung mga standard na pang-hotel service."
        m "Kaya malinis din sa paligid—sanay sila"
        hide Mae_talking
    else:
        show Justine_talking at justine_bottom_left 
        jus "Oo nga, makes sense yung sinabi ni Mae..."
        hide Justine_talking

        scene f6 at Transform(xysize=(2580, 1520)) with fade      
        menu:
            "Try to Open the Door":
                jump door_open
            "Continue walking":
                jump continue_walking

label continue_walking:
    scene housekeeping_room at Transform(xysize=(2580, 1520)) with fade      
    "(Justine glanced at the door one last time, then walked on.)"
    show Justine_happy at justine_bottom_left 
    jus "Wala rin naman akong kailangan dito"
    jus "Pero nice na malaman na hindi lang siya simpleng storage"
    jus "room—training room pala talaga"
    hide Justine_happy

label door_open:
    scene housekeeping_room at Transform(xysize=(2580, 1520)) with fade 
    show Justine_smiling at justine_bottom_left 
    jus "Locked. Yeah... expected"
    jus "Siguro bawal talaga pumasok kung wala kang activity dito"
    jus "Sensitive din kasi gamit—di biro ang linen at cleaning tools ng HM."
    hide Justine_smiling

label fourth_floors2:
    scene f2 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth1
    return
label fourth_floors3:
    scene f3 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth2
    return

label fourth_floors4:
    scene f4 at Transform(xysize=(2580, 1520)) with fade
    scene f5 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth3
    return

label fourth_floors4_1:
    scene f5 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth3
    return

label fourth_floors5:
    scene f6 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth4
    return

label fourth_floors6:
    scene f7 at Transform(xysize=(2580, 1520)) with fade
    call screen fourth5
    return



label csc:
    if not visited_csc:
        $ visited_csc = True
        scene csc_room2 at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left 
        jus "CSC Room."
        jus "Laging naka-lock ‘to tuwing dumadaan ako."
        jus "Pero parang may aura siya na… ‘di ka basta-basta puwedeng pumasok"
        hide Justine_talking
        # Flashback
        show Justine_Sighing at justine_bottom_left 
        jus "Sophie, anong meron dito? Para kasing... ‘secret base."
        hide Justine_Sighing

        show Sophie_talking at right
        s "Haha! In a way, oo."
        s "‘Yan yung office ng Central Student Council. "
        s "Diyan ginagawa lahat ng plans, meetings, at minsan drama rin—lalo pag elections."
        s "May mga whiteboard, mga files, event permits, "
        s "tapos minsan may snacks pa kasi hindi sila natatapos agad."
        s " Diyan naka-base yung mga officers para ayusin events, policies, at minsan... "
        s "mga chismis ng orgs"
        hide Sophie_talking

        show Justine_talking at justine_bottom_left 
        jus "Kaya pala parang ang tahimik pero busy sa loob"
        hide Justine_talking

        show Sophie_smiling at right
        s "Exactly. Kung may problemang student-related"
        s "malamang dito napag-uusapan ‘yon bago makarating sa admin."
        hide Sophie_smiling
    else:
        scene csc_room1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left 
        jus "So, dito ginagawa ang lahat ng desisyon ng mga CSC"
        hide Justine_talking
    jump fourth_floors5

label deluxe_room:
    if not visited_deluxe_room:
        $ visited_deluxe_room = True
        scene
        show Justine_realised at justine_bottom_left 
        jus "De Luxe Room…"
        jus "Grabe, kahit yung pangalan palang, parang bawal mag-ingay, no?"
        hide Justine_realised

        # Flashbac
        show Justine_happy at justine_bottom_left 
        jus "Uy, parang hotel room yung vibe."
        jus "Ano 'to?"
        hide justine_happy

        show Kim_talking at right
        k "Ay, ‘yan yung De Luxe Room!"
        k "Pang-simulation ‘yan ng hotel setup para sa HM students. "
        k "Diyan sila natututo kung paano mag-set up ng real hotel room"
        k "from bed sheets to lighting, pati na rin ‘yung guest interaction."
        k "Kompleto ‘yann—may bed"
        k "CR, vanity area, towels, pillows, like sa real hotels"
        hide Kim_talking

        show Justine_realised at justine_bottom_left 
        jus "Whoa. Kala ko parang show room lang."
        jus "Training area pala talaga."
        hide Justine_realised

        show Kim_happy at right
        k "Yup! Parang practice stage nila para maging legit hotel staff someday"
        k "Kaya sobrang linis at bawal basta-basta pumasok"
        hide Kim_happy
        # End flashback
    else:
        scene 
        show Justine_happy at justine_bottom_left 
        jus "High-end training space pala talaga"
        jus "May pagka-exclusive… pero inspiring rin."
        hide Justine_happy
    jump fourth_floors6
label travel_tours:
    if not visited_travel_tours:
        $ visited_travel_tours = True
        scene travel_and_tours_room1 at Transform(xysize=(2580, 1520)) with fade
        show Justine_happy at justine_bottom_left 
        jus "Travel and Tours Room"
        hide Justine_happy

        show Justine_talking at justine_bottom_left 
        jus "Every time I pass by this room"
        jus "parang naiisip ko agad yung mga airport, plane, at beach."
        jus "Vibe pa lang, parang may adventure"
        hide Justine_talking

        # Flashback
        scene travel_and_tours_room2 at Transform(xysize=(2580, 1520)) with fade
        show Justine_talking at justine_bottom_left 
        jus "Anong meron dito, Jorie? "
        jus "Bakit may mga mini flags saka posters ng mga bansa?"
        hide justine_talking

        show Jorie_talking at right
        j "Ah, ‘yan yung Travel and Tour Room."
        j " Dito nagpa-practice yung Tourism students kung paano maging travel agents"
        j "May mga props pa nga like luggage, destination brochures, at uniforms."
        j "Super hands-on dito!"
        hide Jorie_talking

        show Justine_talking at justine_bottom_left 
        jus "Ayos ah. Parang biyahe without leaving the room."
        hide Justine_talking
    else:
        scene
        show Justine_talking at justine_bottom_left 
        jus "Kaya pala sobrang themed sa loob."
        jus "May mapa pa ng buong mundo sa pader"
    jump fourth_floors6
label standard_room:
    if not visited_standard_room:
        $ visited_standard_room = True
        scene standard_room at Transform(xysize=(2580, 1520)) with fade
        show Justine_happy at justine_bottom_left 
        jus "Mas simple compared sa Deluxe"
        jus "pero may charm parin"
        jus "Parang 'yung classic na kwarto sa probinsya na may aircon"
        hide Justine_happy

        #flashback
        show Justine_talking at justine_bottom_left 
        jus "Akala ko bodega lang ‘to dati. Standard Room pala ang tawag?"
        hide Justine_talking

        show Mae_smiling at right
        m "Haha! Hindi ‘yan bodega, uy. Training room ‘yan ng HM students."
        m "Mas basic siya kaysa sa De Luxe, pero dito muna sila nagpa-practice bago dun"
        m "Diyan nila unang natutunan ‘yung bed making, towel folding, guest essentials setup."
        m "Halos lahat ng firsts nila bilang hotelier, dito nagsisimula"
        hide Mae_smiling

        show Justine_talking at justine_bottom_left 
        jus "So parang ‘foundations room’?"
        hide Justine_talking

        show Mae_talking at right
        m "Exactly. ‘Pag nagkamali ka dito, okay lang"
        m "Dito ka muna matututo bago ka iharap sa mas sosyal na kwarto."
        hide Mae_talking
    else:
        show Justine_talking at justine_bottom_left 
        jus "Makes sense. Dito pala pinapanday ang hospitality skills."
        jus "Every detail counts"
        hide Justine_talking

label stair_roofdeck:
    scene rf1 at Transform(xysize=(2580, 1520)) with fade
    scene rf2 at Transform(xysize=(2580, 1520)) with fade
    scene rf3 at Transform(xysize=(2580, 1520)) with fade
    scene rf4 at Transform(xysize=(2580, 1520)) with fade
    scene rf5 at Transform(xysize=(2580, 1520)) with fade

    show Justine_Sighing at justine_bottom_left
    jus "Di pa ko nakakaalis pero namimiss ko na agad dito."
    hide Justine_Sighing

    show Justine_sad at justine_bottom_left
    jus "Dito kami lagging nag p-p.e at seminar"
    jus "yung tipong di pa nagsisimula ang event o class"
    jus "pero pagod ka na agad sa taas ng a-akysatin mo."
    hide Justine_sad

    show Justine_happy at justine_bottom_left
    jus "Pero worth i naman dahil ma-e-enjoy mo ang view"
    jus "na makikita mo sa galling sa itaas."
    hide Justine_happy

    show Justine_talking at justine_bottom_left
    jus "Makikita mo rito yung mga naglalakihang eroplano at mga magagandang gusali."
    hide Justine_talking

    return

    menu:
        "Go back":
            jump fourth_floors1
        "Don't go back":
            jump main_gate_last

label main_gate_last:
    scene rf6 at Transform(xysize=(2580, 1520)) with fade

    show Justine_sad
    jus "Grabe... tapos ko na lahat."
    jus "Parang ang dami palang lugar dito na dinaanan ko lang dati,"
    jus "pero ngayon… iba na."
    show Justine_crying
    jus "Lahat ng tawanan, pagod, kaba, iyak, at ingay… "
    jus "naiwan na dito sa mga pader, sa sahig, sa hangin"
    jus "Hindi lang pala ito basta campus."
    jus " Ito yung naging background ng halos lahat ng memories ko nitong mga nakaraang taon"
    show Justine_sad
    jus "ang hirap pala magpaalam…"
    jus "pero ang sarap din sa puso"
    show Justine_happy
    jus "kapag alam mong hindi mo sayang ‘yung bawat araw na nandito ka"
    show Justine_sad
    jus "Salamat, PUP Parañaque."
    show Justine_waving
    jus "Sa alaala, sa mga taong nakilala ko, at sa kung sino ako ngayon."

    return 