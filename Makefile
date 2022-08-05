# Variables
I_TESTER = imgft
TESTER = ft_otp

V_CODE = $(PWD)/src:/home/dev/src
V_TEST = $(PWD)/out:/home/dev/out

all: dock
# Ejecuta contenedor creado
exec:
	@docker exec -it $(TESTER) bash

# Genera nuevo contenedor docker
dock: image
	@docker rm -fv $(TESTER) && docker run --name $(TESTER) -v $(V_CODE) -v $(V_TEST) -id $(I_TESTER)

# Genera imagen docker
image:
	@docker build -t $(I_TESTER) .

# Elimina contenedor 
clean:
	@docker rm -fv $(TESTER)

# Elimina imagen
fclean: clean
	@docker rmi $(I_TESTER)

# Elimina y crea una nueva imagen y un nuevo contenedor
re: fclean all 
