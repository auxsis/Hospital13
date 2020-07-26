# -*- coding: utf-8 -*-
{
    'name': "Hospital ",

    'summary': """
       ERP system for Hospital Managemen""",

    'description': """
        complete ERP system for hospital management . you can record patient data ,doctor data,
        lab test record document of patient and many more.
        
    """,

    'author': "Muhammad Danish Hassan",
    'website': "http://www.telenoc.pk",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ["base", "sale_management", "stock", "account", "mail"],

    # always loaded
    'data': [
            'security/hospital_groups.xml',
            'data/ir_sequence_data.xml',
            'views/assets.xml',
            'views/login_page.xml',
            'views/main_menu_file.xml',
             'wizard/medical_appointments_invoice_wizard.xml',
             'wizard/create_prescription_invoice_wizard.xml',
             'wizard/create_prescription_shipment_wizard.xml',
            'views/medical_medicament.xml',
            'views/medical_drug_route.xml',
            'views/medical_imaging_test.xml',
            'views/medical_imaging_test_request.xml',
            'views/medical_imaging_test_type.xml',
            'views/medical_imaging_test_result.xml',
             'wizard/medical_lab_test_create_wizard.xml',
             'wizard/medical_bed_transfer_wizard.xml',
             'wizard/medical_lab_test_invoice_wizard.xml',
             'wizard/appointment_prescription_wizard.xml',
             'views/medical_prescription_order.xml',
            'views/medical_directions.xml',
            'views/medical_dose_unit.xml',
            'views/medical_patient_evaluation.xml',
            'views/medical_family_disease.xml',
            'views/medical_inpatient_registration.xml',
            'views/medical_inpatient_medication.xml',
            'views/medical_insurance_plan.xml',
             'views/medical_appointment.xml',
            'views/medical_insurance.xml',
             'views/medical_patient_lab_test.xml',
            'views/medical_lab_test_units.xml',
             'views/medical_lab.xml',
            'views/medical_neomatal_apgar.xml',
            'views/medical_pathology_category.xml',
            'views/medical_pathology_group.xml',
            'views/medical_pathology.xml',
            'views/medical_patient_disease.xml',
            'views/medical_patient_medication.xml',
            'views/medical_patient_medication1.xml',
            'views/medical_patient_pregnancy.xml',
            'views/medical_patient_prental_evolution.xml',
             'views/medical_patient.xml',
            'views/medical_physician.xml',
            'views/medical_preinatal.xml',
            'views/medical_prescription_line.xml',
            'views/medical_puerperium_monitor.xml',
            'views/medical_rcri.xml',
            'views/medical_rounding_procedure.xml',
            'views/medical_test_critearea.xml',
            'views/medical_test_type.xml',
            'views/medical_vaccination.xml',
            'views/res_partner.xml',
            'report/report_view.xml',
             'report/appointment_recipts_report_template.xml',
             'report/medical_view_report_document_lab.xml',
             'report/medical_view_report_lab_result_demo_report.xml',
            'report/newborn_card_report.xml',
            'report/patient_card_report.xml',
             'report/patient_diseases_document_report.xml',
            'report/patient_medications_document_report.xml',
             'report/patient_vaccinations_document_report.xml',
            'report/prescription_demo_report.xml',
            'security/ir.model.access.csv',
    ],
    'images': ['static/description/hospitalBanner.png'],
    'price': 60.00,
    'currency': 'USD',
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'AGPL-3',
    "installable": True,
    "application": True,
    "auto_install": False,
}
