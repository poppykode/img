
from django.core.paginator import Paginator
from . import models

def paginator(request,qs,number_of_item):
    """
    Creates a paginated view using the provided queryset and per_page setting.
    """
    paginator = Paginator(qs, number_of_item)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj



def save_instruction_bulk(
    station,
    candidate_instruction_heading,
    candidate_instruction_text,
    patient_instruction_heading,
    patient_instruction_text,
):
    if patient_instruction_heading and patient_instruction_text:
        save_instruction(
            station,
            models.PatientInstruction,
            patient_instruction_heading,
            patient_instruction_text,
        )
    if candidate_instruction_heading and candidate_instruction_text:
        save_instruction(
            station,
            models.CandidateInstruction,
            candidate_instruction_heading,
            candidate_instruction_text,
        )


def save_station_approach(
    station, station_approach_learning_points, station_approach_link
):
    if station_approach_learning_points and station_approach_link:
        saved_station_approach = models.StationApproach.objects.create(
            station=station, learning_points=station_approach_learning_points
        )
        station_approach_links_bulk = [
            models.StationApproachLink(
                station_approach=saved_station_approach, link=station_approach_link[i]
            )
            for i in range(len(station_approach_link))
        ]
        models.StationApproachLink.objects.bulk_create(station_approach_links_bulk)


def save_mark_sheet_bulk(
    station, data_gathering_text, management_text, interpersonal_skills_text
):
    if data_gathering_text:
        save_mark_sheet(
            station,
            data_gathering_text,
            models.ExaminerMarkSheet.Heading.DATA_GATHERING,
        )
    if management_text:
        save_mark_sheet(
            station, management_text, models.ExaminerMarkSheet.Heading.MANAGEMENT
        )
    if interpersonal_skills_text:
        save_mark_sheet(
            station,
            interpersonal_skills_text,
            models.ExaminerMarkSheet.Heading.INTERPERSONAL_SKILLS,
        )


def save_mark_sheet(station, text, headings):
    saved_examiner_mark_sheet = models.ExaminerMarkSheet.objects.create(
        station=station, heading=headings
    )
    exam_mark_sheet_answers = [
        models.ExaminerMarkSheetAnswer(
            examiner_mark_sheet=saved_examiner_mark_sheet, answer=text[i]
        )
        for i in range(len(text))
    ]
    models.ExaminerMarkSheetAnswer.objects.bulk_create(exam_mark_sheet_answers)


def save_instruction(station, model, heading, text):
    candidate_bulk = [
        model(station=station, heading=heading[i], text=text[i])
        for i in range(len(text))
    ]
    model.objects.bulk_create(candidate_bulk)
