import xmlrpclib




def logout():

    connection = xmlrpclib.Server('https://ron.respax.com.au:30443/section/xmlrpc/server-ron.php?config=train')


def switch_server(url):

    connection = xmlrpclib.ServerProxy(url)


def get_connection(username, password, server_config):

    url = 'https://ron.respax.com.au:30443/section/xmlrpc/server-ron.php?config='+server_config
    ron = xmlrpclib.ServerProxy(url, allow_none=True)

    try:
        session_id = ron.login(username, password)

        connection = xmlrpclib.ServerProxy(url + '&' + session_id)
        print(connection)
        return {'logic': True, 'session_id': session_id}
    except xmlrpclib.Fault as err:
        return {'logic': False, 'fault': "A fault occurred. Fault code: %d." % err.faultCode +
                                         " Fault string: %s" % err.faultString}


def raw_xml_request(server_url, xml):
    connection = xmlrpclib.ServerProxy(server_url)
    print(xml)
    xml_request = xmlrpclib.loads(xml)
    method = xml_request[xml_request.__len__()-1]
    params = xml_request[0]

    if method == 'ping':
        return connection.ping()

    elif method == 'readHostDetails':
        host_id = params[0]

        host_details = connection.readHostDetails(host_id)
        print(host_details)
        keys = host_details[0].keys()
        xml_response = []
        print(keys)
        for key in keys:
            print(key)
            print(host_details[0][key])

            xml_response.append(str(key) + ': ' + str(host_details[0][key]))

        print(xml_response)
        return xml_response

    elif method == 'readTours':
        host_id = params[0]
        return connection.readTours(host_id)

    elif method == 'readTourDetails':
        host_id = params[0]
        tour_code = params[1]

        return connection.readTourDetails(host_id, tour_code)

    elif method == 'readTourTimes':
        host_id = params[0]
        tour_code = params[1]

        return connection.readTourTimes(host_id, tour_code)

    elif method == 'readTourBases':
        host_id = params[0]
        tour_code = params[1]

        return connection.readTourBases(host_id, tour_code)

    elif method == 'readTourPickups':
        host_id = params[0]
        tour_code = params[1]
        tour_time_id = params[2]
        basis_id = params[3]
        tour_date = params[4]

        return connection.readTourPickups(host_id, tour_code, tour_time_id, basis_id, tour_date)

    elif method == 'readTourPrices':
        host_id = params[0]
        tour_code = params[1]
        basis_id = params[2]
        subbasis_id = params[3]
        tour_date = params[4]
        tour_time_id = params[5]
        pickup_id = params[6]
        drop_off_id = params[7]

        return connection.readTourPrices(host_id, tour_code, basis_id, subbasis_id, tour_date, tour_time_id, pickup_id, drop_off_id)

    elif method == 'readTourPricesRange':
        product_list = []
        #
        # print(connection.readTourPricesRange(product_list))

    elif method == 'readTourAvailability':
        host_id = params[0]
        tour_code = params[1]
        basis_id = params[2]
        subbasis_id = params[3]
        tour_date = params[4]
        tour_time_id = params[5]

        return connection.readTourAvailability(host_id, tour_code, basis_id, subbasis_id, tour_date, tour_time_id)

    elif method == 'readTourAvailabilityRange':
        product_list = params[0]

        return connection.readTourAvailabilityRange(product_list)

    elif method == 'checkReservation':
        host_id = params[0]
        reservation = params[1]
        payment = params[2]

        return connection.checkReservation(host_id, reservation, payment)

    elif method == 'checkReservationAndPrices':
        host_id = params[0]
        reservation = params[1]
        payment = params[2]

        return connection.checkReservationAndPrices(host_id, reservation, payment)


def get_hosts(key, server_url):
    connection = xmlrpclib.ServerProxy(server_url)
    hosts = connection.readHosts()
    list_object = []

    for data in hosts:
        host = (data.get(key, None))
        list_object.append(str(host))

    return list_object


def get_host_details(host_ids, key, server_url):
    connection = xmlrpclib.ServerProxy(server_url)
    list_object = [connection.readHostDetails(data)[0].get(key) for data in host_ids]

    return list_object


def read_tours(host_id, server_url):
    print(host_id)
    print(server_url)
    connection = xmlrpclib.ServerProxy(server_url)

    tours = connection.readTours(host_id)

    return tours


def read_tour_bases(host_id, tour_code, server_url):
    connection = xmlrpclib.ServerProxy(server_url)
    tour_bases = connection.readTourBases(host_id, tour_code)

    return tour_bases


def read_tour_times(host_id, tour_code, server_url):
    connection = xmlrpclib.ServerProxy(server_url)
    tour_times = connection.readTourTimes(host_id, tour_code)

    return tour_times


def read_tour_pickups(host_id, tour_code, tour_time_id, basis_id, server_url):
    connection = xmlrpclib.ServerProxy(server_url)
    tour_pickups = connection.readTourPickups(host_id, tour_code, tour_time_id, basis_id)

    return tour_pickups


