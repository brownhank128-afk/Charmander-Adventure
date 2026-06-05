import streamlit as st
import random
if "pet" not in st.session_state:
    st.session_state.pet = "Charmander"
# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="Charmander Pet",
    page_icon="🔥",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------
if st.session_state.pet == "Charmander":

    st.title("🔥 Ezra's Charmander Pet 🔥")

else:

    st.title("💧 The Flame Went Out... 💧")
# -----------------------------------
# CHARMANDER IMAGE
# -----------------------------------
# -----------------------------------
# SHINY SYSTEM
# -----------------------------------
if "is_shiny" not in st.session_state:

    shiny_roll = random.randint(1, 4096)

    st.session_state.is_shiny = shiny_roll == 1

# -----------------------------------
# SPRITE
# -----------------------------------
if "pet" not in st.session_state:
    st.session_state.pet = "Charmander"
if "pet" not in st.session_state:
    st.session_state.pet = "Charmander"
if st.session_state.pet == "Charmander":

    if st.session_state.is_shiny:

        st.success("✨ SHINY CHARMANDER!!! ✨")

        sprite_url = (
            "https://play.pokemonshowdown.com/sprites/ani-shiny/charmander.gif"
        )

    else:

        sprite_url = (
            "https://play.pokemonshowdown.com/sprites/ani/charmander.gif"
        )

else:

    if st.session_state.is_shiny:

        st.success("✨ SHINY SQUIRTLE!!! ✨")

        sprite_url = (
            "https://play.pokemonshowdown.com/sprites/ani-shiny/squirtle.gif"
        )

    else:

        sprite_url = (
            "https://play.pokemonshowdown.com/sprites/ani/squirtle.gif"
        )

st.image(
    sprite_url,
    width=220
)
# -----------------------------------
# SAVE PET STATS
# -----------------------------------
if "hunger" not in st.session_state:
    st.session_state.hunger = 50

if "energy" not in st.session_state:
    st.session_state.energy = 50

if "happiness" not in st.session_state:
    st.session_state.happiness = 50
if "friendship" not in st.session_state:
    st.session_state.friendship = 1
if "route" not in st.session_state:
    st.session_state.route = "Neutral"
# -----------------------------------
# STATS
# -----------------------------------
st.subheader("📊 Charmander Stats")

# Friendship System
friendship = st.session_state.friendship

friend_title = "🙂 New Friend"

if friendship > 50:
    friend_title = "🔥 Soul Bond 🔥"

elif friendship > 30:
    friend_title = "🐉 Best Friends"

elif friendship > 15:
    friend_title = "😄 Best Buddies"

elif friendship > 5:
    friend_title = "😊 Good Friends"

# Friendship Display
st.write(
f"🔥 Bond Level: {friendship} - {friend_title}"
)

st.progress(min(friendship / 50, 1.0))

st.progress(
    max(0.0, min(st.session_state.hunger / 100, 1.0))
)

st.progress(
    max(0.0, min(st.session_state.energy / 100, 1.0))
)

st.progress(
    max(0.0, min(st.session_state.happiness / 100, 1.0))
)
# -----------------------------------
# BUTTONS
# -----------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🍔 Feed"):
        st.session_state.hunger += 10
        st.session_state.happiness += 5

with col2:
    if st.button("😴 Sleep"):
        st.session_state.energy += 15

with col3:
    if st.button("⚽ Play"):
        st.session_state.happiness += 10
        st.session_state.energy -= 5


# -----------------------------------
# RANDOM MOODS
# -----------------------------------
happy_messages = [
    "Charmander is dancing happily! 🔥",
    "Charmander loves hanging out with Ezra! 😄",
    "Charmander made a tiny fireball! 🔥",
    "Charmander wants snacks! 🍖",
]

sad_messages = [
    "Charmander is tired... 😢",
    "Charmander's tail flame is small... 🔥",
    "Charmander needs attention! 😭",
]

# -----------------------------------
# PET MOOD + REACTIONS
# -----------------------------------
st.subheader("💭 Charmander Mood")
# Route moods
if st.session_state.route == "Bad":

    st.error(
        "Charmander looks kinda hurt... 😭"
    )

elif st.session_state.route == "Good":

    st.success(
        "Charmander trusts Ezra completely ❤️🔥"
    )
mood_face = "😎"
mood_text = "Charmander is feeling good!"

# Hungry
if st.session_state.hunger < 30:
    mood_face = "😭"
    mood_text = "Charmander is REALLY hungry!!"

# Tired
elif st.session_state.energy < 30:
    mood_face = "😴"
    mood_text = "Charmander is sleepy..."

# Super happy
elif st.session_state.happiness > 80:
    mood_face = "🥳"
    mood_text = "Charmander is SUPER excited!"

# Medium happy
elif st.session_state.happiness > 60:
    mood_face = "😄"
    mood_text = "Charmander loves hanging out with Ezra!"

# Display mood
st.header(mood_face)

st.info(mood_text)

# -----------------------------------
# INTERACTIONS
# -----------------------------------
st.subheader("🤝 Interact With Charmander")

interaction = st.selectbox(
    "What do you want to do?",
    [
        "Pet Charmander",
        "Tell a Joke",
        "Dance Together",
        "Roar Like a Dragon",
        "Do Nothing"
    ]
)

if st.button("✨ Interact"):

    if interaction == "Pet Charmander":
        st.success("Charmander purrs happily! 🔥")
        st.session_state.happiness += 5
        st.session_state.friendship += 1

    elif interaction == "Tell a Joke":
        st.info("Charmander laughed so hard he sneezed fire 😂")
        st.session_state.happiness += 10

    elif interaction == "Dance Together":
            st.balloons()
            st.success("You and Charmander did an epic dance battle 💃🔥")
            st.session_state.energy -= 5
            st.session_state.happiness += 15

    elif interaction == "Roar Like a Dragon":
        st.warning("RAAAAAAAWRRRR!!! 🐉🔥")
        st.session_state.energy -= 2

    else:
        st.write("Charmander looks at you awkwardly 👀")
# -----------------------------------
# FAVORITE STARTER EVENT
# -----------------------------------
if st.session_state.friendship >= 10:

    st.subheader("❓ Charmander Has A Question")

    starter_pick = st.radio(
        "who iz ur fav starter?",
        [
            "Charmander 🔥",
            "Squirtle 💧",
            "Bulbasaur 🌱",
            "Pikachu ⚡"
        ],
        index=None
    )

    if st.button("answer question"):

        if starter_pick == "Charmander 🔥":

            st.session_state.route = "Good"

            st.balloons()

            st.success(
                "realy??? YAY!!!!!!! u da best ❤️❤️❤️"
            )

            st.session_state.friendship += 5
            st.session_state.happiness += 15

        elif starter_pick == "Squirtle 💧":

            st.session_state.route = "Bad"

            st.error("...oh. 😭😭😭")

            st.session_state.friendship -= 10
            st.session_state.happiness -= 15

        elif starter_pick == "Bulbasaur 🌱":

            st.warning(
                "bulbasaur iz kinda cool i guess 😐"
            )

        elif starter_pick == "Pikachu ⚡":

            st.info(
                "pikachu wasnt even a starter at first smh 😤"
            )
# -----------------------------------
# SQUIRTLE BATTLE
# -----------------------------------
st.subheader("💧 Squirtle Battle!")

# Create enemy HP
if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 50

st.write(f"💧 Squirtle HP: {st.session_state.enemy_hp}")

st.progress(st.session_state.enemy_hp / 50)

# Attack button
if st.button("🔥 Use Ember"):

    damage = random.randint(5, 15)

    st.session_state.enemy_hp -= damage

    st.success(f"Charmander used EMBER for {damage} damage!! 🔥")

    # Squirtle attacks back
    squirtle_damage = random.randint(1, 10)

    st.session_state.happiness -= squirtle_damage

    st.warning(
        f"Squirtle used Water Gun for {squirtle_damage} damage!! 💧"
    )

# Prevent negative HP
if st.session_state.enemy_hp < 0:
    st.session_state.enemy_hp = 0

# Win condition
if st.session_state.enemy_hp == 0:

    st.balloons()

    st.success("🏆 Charmander defeated Squirtle!!!")

    if st.button("🔄 New Battle"):
        st.session_state.enemy_hp = 50
# -----------------------------------
# FINAL BOSS
# -----------------------------------
if (
    st.session_state.friendship >= 100
    and st.session_state.route == "Good"
):

    st.header("⚔️ FINAL BOSS ⚔️")

    st.error(
        "MEGA SQUIRTLE HAS APPEARED 😭💧"
    )

    # Create boss HP
    if "boss_hp" not in st.session_state:
        st.session_state.boss_hp = 300

    st.write(
        f"💧 Mega Squirtle HP: {st.session_state.boss_hp}"
    )

    st.progress(
        max(
            0.0,
            min(st.session_state.boss_hp / 300, 1.0)
        )
    )

    # Boss attack button
    if st.button("🔥 FINAL EMBER"):

        damage = random.randint(15, 40)

        st.session_state.boss_hp -= damage

        st.success(
            f"MEGA DAMAGE!!! {damage} 🔥"
        )

        # Boss defeated
        if st.session_state.boss_hp <= 0:

            st.balloons()

            st.success(
                "CHARMANDER PROTECTED EVERYONE 😭🔥🏆"
            )

            st.info(
                "TRUE CHARMANDER ENDING ACHIEVED"
            )
# -----------------------------------
# BAD ROUTE ENDING
# -----------------------------------
if (
    st.session_state.friendship >= 100
    and st.session_state.route == "Bad"
):

    st.header("💧 SQUIRTLE ROUTE 💧")

    st.error(
        "Charmander looks really sad... 😭"
    )

    st.write(
        '"i tried really hard 2 be ur favorite..."'
    )

    st.write(
        "💧 Squirtle appeared."
    )

    st.write(
        '"cmon charmander. lets go."'
    )

    if st.button("..."):

        st.session_state.pet = "Squirtle"

        st.success(
            "💧 Squirtle joined your team."
        )
# -----------------------------------
# FINAL STAT LIMITER
# -----------------------------------
st.session_state.hunger = max(
    0,
    min(st.session_state.hunger, 100)
)

st.session_state.energy = max(
    0,
    min(st.session_state.energy, 100)
)

st.session_state.happiness = max(
    0,
    min(st.session_state.happiness, 100)
)

st.session_state.friendship = max(
    0,
    min(st.session_state.friendship, 100)
)
# -----------------------------------
# REROLL SYSTEM
# -----------------------------------
st.subheader("🔄 New Charmander")

# Emotional warnings
if st.session_state.is_shiny:

    st.error(
        "✨ SHINY CHARMANDER DETECTED ✨"
    )

    st.warning(
        "rerolling will delete shiny charmander forever 😭"
    )

elif st.session_state.friendship >= 25:

    st.warning(
        "Charmander: u sure u wanna replace me...? 😭"
    )

# First reroll button
if st.button("✨ reroll charmander"):

    # IMPORTANT rerolls need confirmation
    if (
        st.session_state.is_shiny
        or st.session_state.friendship >= 25
    ):

        st.session_state.confirm_reroll = True

    # Fast rerolls for shiny hunting
    else:

        # Reset stats
        st.session_state.hunger = 50
        st.session_state.energy = 50
        st.session_state.happiness = 50
        st.session_state.friendship = 1

        # New shiny roll
        shiny_roll = random.randint(1, 50)

        st.session_state.is_shiny = (
            shiny_roll == 1
        )

        # Reset battle
        st.session_state.enemy_hp = 50

        # Result
        if st.session_state.is_shiny:

            st.balloons()

            st.success(
                "✨ OMG U GOT A SHINY CHARMANDER ✨"
            )

        else:

            st.info(
                "a new charmander appeared 🔥"
            )

# Confirmation screen
if st.session_state.get("confirm_reroll", False):

    st.subheader("⚠️ FINAL WARNING ⚠️")

    if st.session_state.is_shiny:

        st.error(
            "THIS IS A SHINY CHARMANDER 😭✨"
        )

    st.write(
        "all friendship and progress will reset"
    )

    col1, col2 = st.columns(2)

    # YES reroll
    with col1:

        if st.button("YES reset everything 😭"):

            # Reset stats
            st.session_state.hunger = 50
            st.session_state.energy = 50
            st.session_state.happiness = 50
            st.session_state.friendship = 1

            # New shiny roll
            shiny_roll = random.randint(1, 50)

            st.session_state.is_shiny = (
                shiny_roll == 1
            )

            # Reset battle
            st.session_state.enemy_hp = 50

            # Close confirmation
            st.session_state.confirm_reroll = False

            # Result message
            if st.session_state.is_shiny:

                st.balloons()

                st.success(
                    "✨ OMG NEW SHINY CHARMANDER ✨"
                )

            else:

                st.info(
                    "a new charmander appeared 🔥"
                )

    # CANCEL
    with col2:

        if st.button("NO keep charmander ❤️"):

            st.session_state.confirm_reroll = False

            st.success(
                "Charmander is happy u stayed 😭❤️"
            )