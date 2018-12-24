# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fadiga
import json


def data_json():
    with open("rep_fixtures.json", encoding="utf8") as data_f:
        data = json.loads(data_f.read())
    return data


# def get_imm_code(slug):
#     return get_entities().get(slug).get("imm_code")


def get_offices():
    return data_json().get("offices")


def get_entities():
    return data_json().get("entities")


def get_formes():
    return data_json().get("formes")


def get_postes():
    return data_json().get("postes")


def get_qualities():
    return data_json().get("qualities")


def get_spinneret():
    return data_json().get("spinneret")


def get_activities():
    return data_json().get("activities")


def get_spinneret_activites(act):
    sp_dic = {}
    spinnerets = get_spinneret()
    for slug in spinnerets:
        field = spinnerets[slug]
        activity = field.get("activity")
        if activity == act:
            sp_dic.update({slug: field.get("name")})
    return sp_dic


def get_entity_name(slug):
    return get_entities().get(slug).get("name")


def office_name(slug):
    return get_offices().get(slug).get("name")


def office_region(slug):
    return get_offices().get(slug).get("region")


def office_cercle(slug):
    return get_offices().get(slug).get("cercle")


def regions():
    r_dic = {}
    localities = get_entities()
    for slug in localities:
        field = localities[slug]
        name = field.get("name")
        type = field.get("type")
        if type == 'region':
            r_dic.update({slug: name})
    return r_dic


def entity_children(p_slug):
    c_dic = {}
    localities = get_entities()
    for slug in localities:
        field = localities[slug]
        parent = field.get("parent")
        name = field.get("name")
        if parent == p_slug:
            c_dic.update({slug: name})
    return c_dic
