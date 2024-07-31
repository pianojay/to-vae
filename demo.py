from FEA_compliance import main as fea_compliance

""" To do:
        Sample encoded to latent vector
        Agent "modifies" latent vector
        latent vector decoded to design space
        Compliance for the model.
"""

""" Prerequisites:
        Pre-trained VAE model
        Sample (can be anything)
        "Agent"
        Compliance conditions
"""

vae_model = None # Pretrained...

initial_input = None # examplary initialization, started by encoding (not necessary to start from here.)

latent_vector = vae_model.encode(initial_input)

agent = None


# The following is the training procedure

while agent.ch>0.01:
    
    next_latent_vector = agent(latent_vector)

    modified_output = vae_model.decode(next_latent_vector)

    compliance = fea_compliance(modified_output) # with other conditions

    critic = None # from environment

    score = critic()

    agent.feedback(compliance)

    latent_vector = next_latent_vector