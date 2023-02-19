import os
import openai 
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = "Compare the `response` to the `answer` considering the `params`. Output your answer in exactly and only the following format: \n{{\n\"command\": \"eval\",\n\"result\":{{\n\"is_correct\": \"<bool>\",\n\"feedback\":\"<string>\",\n\"warnings\": \"<array>\"\n}}\n}} \n Answer: {}. \n Response: {}. \n params: {}. \n Only provide corrective or suggestive feedback. Don't provide any subjective, emotional, or motivational feedback (such as exclamation marks or 'well done'). Don't reveal the true answer if it wasn't given in the response.".format("A Newtonian fluid is a fluid in which the viscous stresses arising from its flow are at every point linearly correlated to the local strain rate — the rate of change of its deformation over time. Stresses are proportional to the rate of change of the fluid's velocity vector.\n A fluid is Newtonian only if the tensors that describe the viscous stress and the strain rate are related by a constant viscosity tensor that does not depend on the stress state and velocity of the flow. If the fluid is also isotropic (mechanical properties are the same along any direction), the viscosity tensor reduces to two real coefficients, describing the fluid\'s resistance to continuous shear deformation and continuous compression or expansion, respectively.\n Newtonian fluids are the simplest mathematical models of fluids that account for viscosity. While no real fluid fits the definition perfectly, many common liquids and gases, such as water and air, can be assumed to be Newtonian for practical calculations under ordinary conditions. However, non-Newtonian fluids are relatively common and include oobleck (which becomes stiffer when vigorously sheared) and non-drip paint (which becomes thinner when sheared). Other examples include many polymer solutions (which exhibit the Weissenberg effect), molten polymers, many solid suspensions, blood, and most highly viscous fluids.\n Newtonian fluids are named after Isaac Newton, who first used the differential equation to postulate the relation between the shear strain rate and shear stress for such fluids.","A fluid which is sticky",{"Important":"'Constant shear stress' is not correct","GiveCorrectAnswerIfIncorrect":"Never","HintIfTotallyWrong":"Look at Lecture 10 for the definition; or try a textbook or Wikipedia."})

response = openai.Completion.create(
engine="text-davinci-002",
prompt=prompt,
max_tokens=1024,
)

result=json.loads(response.choices[0].to_dict()["text"].replace("\n",""))

print(result)