from django_elasticsearch_dsl_drf.filter_backends import (
    CompoundSearchFilterBackend,
    DefaultOrderingFilterBackend,
    HighlightBackend,
    FilteringFilterBackend,
    NestedFilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    SuggesterFilterBackend,
    PostFilterFilteringFilterBackend,
    FacetedSearchFilterBackend,
    SearchFilterBackend,
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination

from search.documents.post import PostDocument
from search.serializers.post import PostDocumentSerializer
from utils.permissions import ReadOnly

from search.backends.multi_match_filter import MultiMatchSearchFilterBackend

class PostDocumentView(DocumentViewSet):
    document = PostDocument
    permission_classes = [ReadOnly]
    serializer_class = PostDocumentSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'id'
    filter_backends = [
        MultiMatchSearchFilterBackend,
        CompoundSearchFilterBackend,
        FacetedSearchFilterBackend,
        FilteringFilterBackend,
        PostFilterFilteringFilterBackend,
        DefaultOrderingFilterBackend,
        OrderingFilterBackend,
        HighlightBackend,
    ]

    search_fields = {
        'title': {'boost': 2, 'fuzziness': 1},
        'renderable_text': {'boost': 1, 'fuzziness': 1},
        'hubs_flat': {'boost': 1, 'fuzziness': 1},
    }

    multi_match_search_fields = {
        'title': {'boost': 2},
        'renderable_text': {'boost': 1},
        'hubs_flat': {'boost': 1},
    }

    multi_match_options = {
        'operator': 'and',
        'type': 'best_fields',
    }

    post_filter_fields = {
        'hubs': 'hubs.name',
    }

    faceted_search_fields = {
        'hubs': 'hubs.name'
    }

    filter_fields = {
        'publish_date': 'created_date'
    }

    ordering = ('_score', '-hot_score', '-discussion_count', '-created_date')

    ordering_fields = {
        'publish_date': 'created_date',
        'discussion_count': 'discussion_count',
        'score': 'score',
        'hot_score': 'hot_score',
    }

    highlight_fields = {
        'title': {
            'enabled': True,
            'options': {
                'pre_tags': ["<mark>"],
                'post_tags': ["</mark>"],
                'fragment_size': 2000,
                'number_of_fragments': 1,
            },
        },
        'renderable_text': {
            'enabled': True,
            'options': {
                'pre_tags': ["<mark>"],
                'post_tags': ["</mark>"],
                'fragment_size': 5000,
                'number_of_fragments': 1,
            },
        }
    }

