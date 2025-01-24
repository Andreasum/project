from PIL import Image
import requests
import streamlit as st


st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")




st.subheader("Hello my name is Andrea Suma and this is an aducational website that talks about the rise and fall of the Roman Empire.")
st.title("The rise of the Roman Empire")




with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("")
        st.write("##")
        st.write(
            """
           1. Augustus and the Beginning of the Empire (27 BCE)
In 27 BCE, Octavian became the first Roman emperor, taking the title Augustus. This marked the transition from the Roman Republic to the Roman Empire. 

Augustus consolidated power, controlled the military, and established a period of peace and stability known as the Pax Romana. 
His reforms included creating a professional standing army and improving Roman infrastructure.

2. The Julio-Claudian Dynasty (14–68 CE)
After Augustus, the Julio-Claudian Dynasty ruled Rome, starting with Tiberius. 
Despite some emperors like Caligula and Nero being notorious for cruelty, emperors like Claudius expanded the empire, while Nero's reign saw cultural developments but ended with his suicide in 68 CE.

3. The Flavian Dynasty (69–96 CE)
Following a period of civil war, the Flavian Dynasty began with Vespasian. 
The dynasty saw significant building projects like the Colosseum and military successes. 
Titus and Domitian continued these efforts, but Domitian’s autocratic rule ended with his assassination.

4. The Five Good Emperors (96–180 CE)
The Five Good Emperors were known for their effective and benevolent rule. 
Trajan expanded the empire to its greatest extent, Hadrian secured the borders, and Marcus Aurelius, a philosopher-emperor, led during difficult wars. 
This period marked the peak of Roman power, with military victories and flourishing culture.

5. Cultural and Economic Growth
During this time, Rome saw impressive architecture (like the Pantheon and Colosseum), flourishing literature (with writers like Virgil), and a strong economy based on trade and infrastructure.

        If you are interested in more details about the ris of the empire you can click the link below to a history youtube channel.
            """

        )
        st.write("[YouTube Channel >](https://www.youtube.com/@TheInfographicsShow)")


with st.container():
    st.write("---")
    st.header("")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    
    with image_column:
        img = Image.open("images\Roman.png")
        st.image(
            img ,
            caption="" ,
            width= 400 ,
            channels= "RGB"
        )
    
    
        
    with text_column:
        st.subheader("The fall of the Roman Empire")
        st.write(
            """
            The fall of the Roman Empire is a complex and multifaceted event that occurred over several centuries, with numerous contributing factors.
             
            Historians debate the exact reasons, but here are some of the main causes that are generally agreed upon:

            Economic Decline: The Roman Empire faced severe economic problems, including heavy taxation, inflation, and reliance on slave labor. 

                The economy struggled to sustain the vast empire, and the wealth gap between the rich and poor widened, leading to social unrest.

            Political Corruption and Instability: The Roman political system became increasingly corrupt, with a lack of effective leadership and frequent changes in emperors.

                Civil wars, assassinations, and power struggles weakened the empire’s ability to respond to external threats.

            Military Problems: The Roman military, once a highly organized and disciplined force, faced issues such as overextension, and constant pressure from invading barbarian tribes. 

                The empire had trouble defending its vast borders.

            Barbarian Invasions: Various "barbarian" groups, such as the Visigoths, Vandals, Huns, and Franks, repeatedly invaded the Roman Empire. 

            Division of the Empire: In 285 AD, Emperor Diocletian split the Roman Empire into two parts: the Western Roman Empire and the Eastern Roman Empire (Byzantine Empire). 
            
            While the Eastern Roman Empire thrived for many more centuries, the Western Roman Empire became more vulnerable to internal and external pressures, leading to its eventual collapse.

            Cultural and Religious Shifts: The rise of Christianity changed the cultural landscape of the empire. 

                Some argue that the adoption of Christianity in the 4th century led to the decline of traditional Roman values and the unity of the empire. 
                
                Others believe Christianity helped the empire's survival by providing a unifying force, though it did lead to changes in the political and social fabric.

            Overextension and Overpopulation: The empire was simply too large to manage effectively. The vast territorial expanse of Rome became increasingly difficult to govern, maintain, and defend.

             The population also became too large to be supported by the empire's resources.

            In summary, the fall of the Roman Empire was due to a combination of internal weaknesses and external pressures. The empire didn’t fall overnight, but gradually crumbled under the weight of these challenges. 

                The Eastern Roman Empire, centered in Constantinople, continued for nearly another thousand years as the Byzantine Empire, lasting until 1453 AD.

                
            If you are interested in more details about the fall of the Roman Empire you can click the link below to watch a video.
            
            """
        ) 
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=5tilhR0C6DY&t=2s)")



with st.container():
    st.write("---")
    st.header("If you find any mistakes in this website you are free to send me an email below and I will make sure to fix it")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/andrea.suma.2004.as@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()