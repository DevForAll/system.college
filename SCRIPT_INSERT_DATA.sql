INSERT INTO public.tpp_usuario(
	vc_nombre, vc_apellido_parterno, vc_apellido_materno, vc_codigo, vc_usuario, vc_password,
	in_tipo_documento, dt_nacimiento, vc_pais, vc_departamento, vc_provincia, vc_distrito, vc_direccion, 
	dt_registry, vc_celular, vc_correo)
	VALUES ('Abril', 'Peralta', 'Valenzuela', '2021000003', 'abril peralta', '2021000003',1, '2004-04-03', 'Peru', 'Lima', 'Lima', 'Miraflores', 'Pituca city', '2021-06-07 23:30:00.00', '+51 921465854', 'abril.peralta@gmail.com');

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