INSERT INTO public.tpp_usuario(
	vc_nombre, vc_apellido_parterno, vc_apellido_materno, vc_codigo, vc_usuario, vc_password,
	in_tipo_documento, dt_nacimiento, vc_pais, vc_departamento, vc_provincia, vc_distrito, vc_direccion, 
	dt_registry, vc_celular, vc_correo)
	VALUES ('Pedro', 'Castillo', 'Ladron', '2021000003', 'pedro castillo', '2021000003',
			1, '1975-05-06', 'Peru', 'Puno', 'Puno', 'Chanchallo', 'Cerro', 
			'2021-06-05 22:57:00.54', '+51 995485742', 'pedro.castillo@gmail.com');

SELECT*FROM TPP_USUARIO;

INSERT INTO public.tpp_roles(
	in_idtipo_usuario, in_idusuario)
	VALUES (2, 1);
INSERT INTO public.tpp_roles(
	in_idtipo_usuario, in_idusuario)
	VALUES (2, 2);
INSERT INTO public.tpp_roles(
	in_idtipo_usuario, in_idusuario)
	VALUES (2, 3);
INSERT INTO public.tpp_roles(
	in_idtipo_usuario, in_idusuario)
	VALUES (3, 4);

SELECT*FROM TPP_ROLES;
SELECT*FROM TPP_TIPO_USUARIO;